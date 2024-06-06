import requests
import aiohttp
import asyncio

base_url = [
    "http://192.168.6.153:8000/",
    "http://192.168.6.155:8000/",
    "http://192.168.6.156:8000/",
    "http://192.168.6.160:8000/",
    "http://192.168.6.161:8000/",
]


async def camera_req(url, msg):
    async with aiohttp.ClientSession() as session:
        async with session.get(url + msg) as response:
            data = await response
            print(data)
            return data


# async def start_camera():
#     global base_url
#     response = {}
#     for i, url in enumerate(base_url):
#         res = await requests.get(url + str("start_capture"))
#         print(res["message"])
#         response[i + 1] = res["message"]
#     return response


# async def stop_capture():
#     global base_url
#     response = {}
#     for i, url in enumerate(base_url):
#         res = await requests.get(url + str("stop_capture"))
#         print(res["message"])
#         response[i + 1] = res["message"]
#     return response


async def main(msg):
    global base_url
    res = {}
    for i, url in enumerate(base_url):
        response = await camera_req(url, str(msg))
        print(response)


asyncio.run(main("start_capture"))
