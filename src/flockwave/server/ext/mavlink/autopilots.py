"""Implementations of autopilot-specific functionality."""

from abc import ABCMeta, abstractmethod
from typing import Type

from flockwave.server.model.geofence import GeofenceAction, GeofenceStatus

from .enums import MAVAutopilot, MAVProtocolCapability
from .geofence import GeofenceManager
from .types import MAVLinkMessage


class Autopilot(metaclass=ABCMeta):
    """Interface specification and generic entry point for autopilot objects."""

    name = "Abstract autopilot"

    def __init__(self, base=None) -> None:
        self.capabilities = int(getattr(base, "capabilities", 0))

    @staticmethod
    def from_autopilot_type(type: int) -> Type["Autopilot"]:
        """Returns an autopilot class suitable to represent the behaviour of
        an autopilot with the given MAVLink autopilot identifier in the
        heartbeat message.
        """
        return _autopilot_registry.get(type, UnknownAutopilot)

    @classmethod
    def from_heartbeat(cls, message: MAVLinkMessage) -> Type["Autopilot"]:
        """Returns an autopilot class suitable to represent the behaviour of
        an autopilot with the given MAVLink heartbeat message.
        """
        return cls.from_autopilot_type(message.autopilot)

    @classmethod
    def describe_mode(cls, base_mode: int, custom_mode: int) -> str:
        """Returns the description of the current mode that the autopilot is
        in, given the base and the custom mode in the heartbeat message.
        """
        if base_mode & 1:
            # custom mode
            return cls.describe_custom_mode(base_mode, custom_mode)
        elif base_mode & 4:
            # auto mode
            return "auto"
        elif base_mode & 8:
            # guided mode
            return "guided"
        elif base_mode & 16:
            # stabilize mode
            return "stabilize"
        elif base_mode & 64:
            # manual mode
            return "manual"

    @classmethod
    def describe_custom_mode(cls, base_mode: int, custom_mode: int) -> str:
        """Returns the description of the current custom mode that the autopilot
        is in, given the base and the custom mode in the heartbeat message.

        This method is called if the "custom mode" bit is set in the base mode
        of the heartbeat.
        """
        return f"mode {custom_mode}"

    @abstractmethod
    async def get_geofence_status(self, uav) -> GeofenceStatus:
        """Retrieves a full geofence status object from the drone.

        Parameters:
            uav: the MAVLinkUAV object

        Returns:
            a full geofence status object

        Raises:
            NotImplementedError: if we have not implemented support for retrieving
                the geofence status from the autopilot (but it supports
                geofences)
            NotSupportedError: if the autopilot does not support geofences at all
        """
        raise NotImplementedError

    def refine_with_capabilities(self, capabilities: int):
        """Refines the autopilot class with further information from the
        capabilities bitfield of the MAVLink "autopilot capabilities" message,
        returning a new autopilot instance if the autopilot type can be narrowed
        further by looking at the capabilities.
        """
        self.capabilities = capabilities
        return self


class UnknownAutopilot(Autopilot):
    """Class representing an autopilot that we do not know."""

    name = "Unknown autopilot"

    async def get_geofence_status(self, uav) -> GeofenceStatus:
        raise NotImplementedError


class ArduPilot(Autopilot):
    """Class representing the ArduPilot autopilot firmware."""

    name = "ArduPilot"
    _custom_modes = {
        0: "stabilize",
        1: "acro",
        2: "alt hold",
        3: "auto",
        4: "guided",
        5: "loiter",
        6: "rth",
        7: "circle",
        9: "land",
        11: "drift",
        13: "sport",
        14: "flip",
        15: "tune",
        16: "pos hold",
        17: "brake",
        18: "throw",
        19: "avoid ADSB",
        20: "guided no GPS",
        21: "smart RTH",
        22: "flow hold",
        23: "follow",
        24: "zigzag",
        25: "system ID",
        26: "heli autorotate",
    }

    _geofence_actions = {
        0: (GeofenceAction.REPORT,),
        1: (GeofenceAction.RETURN, GeofenceAction.LAND),
        2: (GeofenceAction.LAND,),
        3: (GeofenceAction.SMART_RETURN, GeofenceAction.RETURN, GeofenceAction.LAND),
        4: (GeofenceAction.STOP, GeofenceAction.LAND),
    }

    @classmethod
    def describe_custom_mode(cls, base_mode: int, custom_mode: int) -> str:
        """Returns the description of the current custom mode that the autopilot
        is in, given the base and the custom mode in the heartbeat message.

        This method is called if the "custom mode" bit is set in the base mode
        of the heartbeat.
        """
        return cls._custom_modes.get(custom_mode, f"mode {custom_mode}")

    async def get_geofence_status(self, uav) -> GeofenceStatus:
        status = GeofenceStatus()

        # Generic stuff comes here
        manager = GeofenceManager.for_uav(uav)
        await manager.get_geofence_areas_and_rally_points(status)

        # ArduCopter-specific parameters are used to extend the status
        value = await uav.get_parameter("FENCE_ENABLE")
        status.enabled = bool(value)

        value = await uav.get_parameter("FENCE_ALT_MIN")
        status.min_altitude = float(value)

        value = await uav.get_parameter("FENCE_ALT_MAX")
        status.max_altitude = float(value)

        value = await uav.get_parameter("FENCE_RADIUS")
        status.max_distance = float(value)

        value = await uav.get_parameter("FENCE_ACTION")
        status.actions = list(self._geofence_actions.get(value, ()))

        return status

    def refine_with_capabilities(self, capabilities: int):
        result = super().refine_with_capabilities(capabilities)

        if isinstance(result, self.__class__) and not isinstance(
            result, ArduPilotWithSkybrush
        ):
            mask = ArduPilotWithSkybrush.CAPABILITY_MASK
            if (capabilities & mask) == mask:
                result = ArduPilotWithSkybrush(self)

        return result


def extend_custom_modes(super, _new_modes, **kwds):
    """Helper function to extend the custom modes of an Autopilot_ subclass
    with new modes.
    """
    result = dict(super._custom_modes)
    result.update(_new_modes)
    result.update(**kwds)
    return result


class ArduPilotWithSkybrush(ArduPilot):
    """Class representing the ArduCopter firmware with Skybrush-specific
    extensions to support drone shows.
    """

    name = "ArduPilot + Skybrush"
    _custom_modes = extend_custom_modes(ArduPilot, {127: "show"})

    CAPABILITY_MASK = (
        MAVProtocolCapability.PARAM_FLOAT
        | MAVProtocolCapability.FTP
        | MAVProtocolCapability.SET_POSITION_TARGET_GLOBAL_INT
        | MAVProtocolCapability.SET_POSITION_TARGET_LOCAL_NED
        | MAVProtocolCapability.MAVLINK2
        | MAVProtocolCapability.DRONE_SHOW_MODE
    )


_autopilot_registry = {MAVAutopilot.ARDUPILOTMEGA: ArduPilot}
