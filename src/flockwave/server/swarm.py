import socket,time,csv
from math import radians,cos,sin,sqrt,atan2

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("",12009))

master_num=0
#udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address1 = ('192.168.29.151', 12008)
#udp_socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address2 = ('192.168.29.152', 12008)
udp_socket3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address3 = ('192.168.29.153', 12008)
#udp_socket4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address4 = ('192.168.29.154', 12008)
udp_socket5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address5 = ('192.168.29.155', 12008)
#udp_socket6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address6 = ('192.168.29.156', 12008)
#udp_socket7 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address7 = ('192.168.29.157', 12008)
#udp_socket8 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address8 = ('192.168.29.158', 12008)
#udp_socket9 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address9 = ('192.168.29.159', 12008)
udp_socket10 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address10 = ('192.168.29.160', 12008)

#share_data_udp_socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#share_data_server_address1 = ('192.168.29.151', 12008)
#share_data_udp_socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#share_data_server_address2 = ('192.168.29.152', 12008)
share_data_udp_socket3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
share_data_server_address3 = ('192.168.29.153', 12008)
#share_data_udp_socket4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#share_data_server_address4 = ('192.168.29.154', 12008)
share_data_udp_socket5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
share_data_server_address5 = ('192.168.29.155', 12008)
#udp_socket6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address6 = ('192.168.29.156', 12008)
#share_data_udp_socket7 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#share_data_server_address7 = ('192.168.29.157', 12008)
#udp_socket8 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address8 = ('192.168.29.158', 12008)
#udp_socket9 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address9 = ('192.168.29.159', 12008)
share_data_udp_socket10 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
share_data_server_address10 = ('192.168.29.160', 12008)

#socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address11 = ('192.168.29.151', 12002)
#socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address12 = ('192.168.29.152', 12002)
socket3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address13 = ('192.168.29.153', 12002)
#socket4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address14 = ('192.168.29.154', 12002)
socket5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address15 = ('192.168.29.155', 12002)
#socket6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address16 = ('192.168.29.156', 12002)
#socket7 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address17 = ('192.168.29.157', 12002)
#socket8 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address18 = ('192.168.29.158', 12002)
#socket9 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address19 = ('192.168.29.159', 12002)
socket10 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address20 = ('192.168.29.160', 12002)

#file_sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#file_server_address1 = ('192.168.29.151', 12003)  
#file_sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#file_server_address2 = ('192.168.29.152', 12003)
file_sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
file_server_address3 = ('192.168.29.153', 12003)
#file_sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#file_server_address4 = ('192.168.29.154', 12003)
file_sock5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
file_server_address5 = ('192.168.29.155', 12003)
#file_sock6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#file_server_address6 = ('192.168.29.156', 12003)
#file_sock7 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#file_server_address7 = ('192.168.29.157', 12003)
#file_sock8 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#file_server_address8 = ('192.168.29.158', 12003)
#file_sock9 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#file_server_address9 = ('192.168.29.159', 12003)
file_sock10 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
file_server_address10 = ('192.168.29.160', 12003)

'''
mavlink_sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mavlink_server_address1 = ('192.168.29.151', 12045)

mavlink_sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mavlink_server_address2 = ('192.168.29.152', 12045)
'''
mavlink_sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mavlink_server_address3 = ('192.168.29.153', 12045)

#mavlink_sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#mavlink_server_address4 = ('192.168.29.154', 12045)

mavlink_sock5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mavlink_server_address5 = ('192.168.29.155', 12045)

#mavlink_sock6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#mavlink_server_address6 = ('192.168.29.156', 12045)

#mavlink_sock7 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#mavlink_server_address7 = ('192.168.29.157', 12045)

#mavlink_sock8 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#mavlink_server_address8 = ('192.168.29.158', 12045)

#mavlink_sock9 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#mavlink_server_address9 = ('192.168.29.159', 12045)

mavlink_sock10 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mavlink_server_address10 = ('192.168.29.160', 12045)

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points
    on the Earth's surface using the Haversine formula.

    Parameters:
    - lat1, lon1: Latitude and longitude of the first point (in degrees).
    - lat2, lon2: Latitude and longitude of the second point (in degrees).

    Returns:
    - The distance between the two points (in meters).
    """
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371000 * c  # Radius of Earth in meters

    return distance

def calculate_flight_time():
    global flight_time_var,csv_files
    total_distance = 0
    num_uavs = 0

    for uav, csv_path in csv_files.items():
        lat_lon_points = []
        with open(csv_path, 'rt') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header (first row)
            for row in csv_reader:
                lat, lon = map(float, row)
                lat_lon_points.append((lat, lon))

        total_distance_uav = 0
        for i in range(len(lat_lon_points) - 1):
            lat1, lon1 = lat_lon_points[i]
            lat2, lon2 = lat_lon_points[i + 1]
            distance = haversine(lat1, lon1, lat2, lon2)
            total_distance_uav += distance

        total_distance += total_distance_uav
        num_uavs += 1

    average_total_distance = total_distance / num_uavs
    average_speed = 3  # Assume average speed between 4 m/s and 5 m/s
    flight_time_seconds = average_total_distance / average_speed
    flight_time_minutes = flight_time_seconds / 60

    flight_time_var.set("Flight Time = {:.2f} minutes".format(flight_time_minutes))


def clear_csv():
    print("!!!CSV Cleared!!")
    global udp_socket,udp_socket2,server_address1,server_address2
    #udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = "clear_csv"
    '''
    udp_socket.sendto(str(data).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(data).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(data).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(data).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(data).encode(), server_address5)
    time.sleep(0.5)
    '''       
    udp_socket6.sendto(str(data).encode(), server_address6)
    time.sleep(0.5)       
    udp_socket7.sendto(str(data).encode(), server_address7)     
    time.sleep(0.5)
    udp_socket8.sendto(str(data).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(data).encode(), server_address9)
    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(data).encode(), server_address10)

def start_socket():
    print("!!!Start!!")
    global udp_socket,udp_socket2,server_address1,server_address2
    #udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = "start"
    '''
    udp_socket.sendto(str(data).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(data).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(data).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(data).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(data).encode(), server_address5)
    time.sleep(0.5)
    '''
    udp_socket6.sendto(str(data).encode(), server_address6)
    time.sleep(0.5)

    udp_socket7.sendto(str(data).encode(), server_address7)
    time.sleep(0.5)

    udp_socket8.sendto(str(data).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(data).encode(), server_address9)
    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(data).encode(), server_address10)
    
    return True


def start1_socket():
    print("Start1........")
    global udp_socket,server_address1,server_address2,udp_socket2
    #udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = "start1"
    '''
    udp_socket.sendto(str(data).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(data).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(data).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(data).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(data).encode(), server_address5)
    time.sleep(0.5)
    '''
    udp_socket6.sendto(str(data).encode(), server_address6)
    time.sleep(0.5)

    udp_socket7.sendto(str(data).encode(), server_address7)

    time.sleep(0.5)
    udp_socket8.sendto(str(data).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(data).encode(), server_address9)
    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(data).encode(), server_address10)

def home_lock():
    print("Home position Locked....!!!!")
    global udp_socket,server_address1,server_address2,udp_socket2
    #udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = "home_lock"
    '''
    udp_socket.sendto(str(data).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(data).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(data).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(data).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(data).encode(), server_address5)
    time.sleep(0.5)
    '''
    udp_socket6.sendto(str(data).encode(), server_address6)
    time.sleep(0.5)

    udp_socket7.sendto(str(data).encode(), server_address7)

    time.sleep(0.5)
    udp_socket8.sendto(str(data).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(data).encode(), server_address9)
    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(data).encode(), server_address10)

def select_plot(filename):
    if filename!="":
    
        '''
        file_sock1.sendto(str(filename).encode(),file_server_address1)
        time.sleep(0.5)
        file_sock2.sendto(str(filename).encode(),file_server_address2)
        time.sleep(0.5)
        '''
        file_sock3.sendto(str(filename).encode(),file_server_address3)
        time.sleep(0.5)
        '''
        file_sock4.sendto(str(filename).encode(),file_server_address4)
        time.sleep(0.5)
        '''
        file_sock5.sendto(str(filename).encode(),file_server_address5)
        time.sleep(0.5)
        '''
        file_sock6.sendto(str(filename).encode(),file_server_address6)
        time.sleep(0.5)

        file_sock7.sendto(str(filename).encode(),file_server_address7)		
        time.sleep(0.5)

        file_sock8.sendto(str(filename).encode(),file_server_address8)
        time.sleep(0.5)
        file_sock9.sendto(str(filename).encode(),file_server_address9)
        time.sleep(0.5)
        '''
        file_sock10.sendto(str(filename).encode(),file_server_address10)


def share_data_func(goal_table,return_goal_table,grid_path_table):
    #global goal_table,return_goal_table,filename,udp_socket,server_address1,server_address2,udp_socket2,grid_path_table
    print("*******",goal_table) 
    #goal_table=[]

    if return_goal_table is not None:
        combined_goal_table = goal_table + return_goal_table 
        print("combined_goal_table",combined_goal_table)
        '''
        share_data_udp_socket1.sendto(("share_data" + "," + str(combined_goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address1)
        time.sleep(0.5)
        share_data_udp_socket2.sendto(("share_data" + "," + str(combined_goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address2)
        time.sleep(0.5)
        '''
        share_data_udp_socket3.sendto(("share_data" + "," + str(combined_goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address3)
        time.sleep(0.5)
        '''
        share_data_udp_socket4.sendto(("share_data" + "," + str(combined_goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address4)
        time.sleep(0.5)
        '''
        share_data_udp_socket5.sendto(("share_data" + "," + str(combined_goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address5)
        time.sleep(0.5)
        '''
        share_data_udp_socket6.sendto(("share_data" + "," + str(combined_goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address6)
        time.sleep(0.5)

        share_data_udp_socket7.sendto(("share_data" + "," + str(combined_goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address7)

        time.sleep(0.5)
        share_data_udp_socket8.sendto(("share_data" + "," + str(combined_goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address8)
        time.sleep(0.5)
        share_data_udp_socket9.sendto(("share_data" + "," + str(combined_goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address9)
        time.sleep(0.5)
        '''
        share_data_udp_socket10.sendto(("share_data" + "," + str(combined_goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address10)

    else:

        '''
        share_data_udp_socket1.sendto(("share_data"+","+ str(goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address1)
        time.sleep(0.5)
        share_data_udp_socket2.sendto(("share_data"+","+ str(goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address2)
        time.sleep(0.5)
        '''
        share_data_udp_socket3.sendto(("share_data"+","+ str(goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address3)
        time.sleep(0.5)
        '''
        share_data_udp_socket4.sendto(("share_data"+","+ str(goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address4)
        time.sleep(0.5)
        '''
        share_data_udp_socket5.sendto(("share_data"+","+ str(goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address5)
        time.sleep(0.5)
        '''
        share_data_udp_socket6.sendto(("share_data"+","+ str(goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address6)
        time.sleep(0.5)

        share_data_udp_socket7.sendto(("share_data"+","+ str(goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address7)

        time.sleep(0.5)
        share_data_udp_socket8.sendto(("share_data"+","+ str(goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address8)
        time.sleep(0.5)
        share_data_udp_socket9.sendto(("share_data"+","+ str(goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address9)
        time.sleep(0.5)
        '''
        share_data_udp_socket10.sendto(("share_data"+","+ str(goal_table)+","+"grid_path_table" +","+str( grid_path_table)).encode(), share_data_server_address10)


def disperse_socket(): 
    global udp_socket,server_address1,server_address2,udp_socket2
    print("Disperse!!!!!!")
    #udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = "disperse"
    '''
    udp_socket.sendto(str(data).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(data).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(data).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(data).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(data).encode(), server_address5)
    time.sleep(0.5)
    '''
    udp_socket6.sendto(str(data).encode(), server_address6)
    time.sleep(0.5)

    udp_socket7.sendto(str(data).encode(), server_address7)

    time.sleep(0.5)
    udp_socket8.sendto(str(data).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(data).encode(), server_address9)
    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(data).encode(), server_address10)


def takeoff_socket(alt):
    print("Takeoff...........")
    takeoff_alt = alt
    global udp_socket,server_address1,server_address2,udp_socket2
    #udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = "takeoff"+","+str(takeoff_alt)
    '''
    sent = udp_socket.sendto(str(data).encode(), server_address1)
    time.sleep(0.5)
    sent = udp_socket2.sendto(str(data).encode(), server_address2)
    time.sleep(0.5)
    '''
    sent = udp_socket3.sendto(str(data).encode(), server_address3)
    time.sleep(0.5)
    '''
    sent = udp_socket4.sendto(str(data).encode(), server_address4)
    time.sleep(0.5)
    '''
    sent = udp_socket5.sendto(str(data).encode(), server_address5)     
    time.sleep(0.5)
    '''
    sent = udp_socket6.sendto(str(data).encode(), server_address6)
    time.sleep(0.5)

    sent = udp_socket7.sendto(str(data).encode(), server_address7)

    time.sleep(0.5)
    sent = udp_socket8.sendto(str(data).encode(), server_address8)
    time.sleep(0.5)
    sent = udp_socket9.sendto(str(data).encode(), server_address9)

    time.sleep(0.5)
    '''
    sent = udp_socket10.sendto(str(data).encode(), server_address10)

def search_socket(): 
    global udp_socket,server_address1,server_address2,udp_socket2
    print("Searching........")
    #udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = "search"
    '''
    udp_socket.sendto(str(data).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(data).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(data).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(data).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(data).encode(), server_address5)

    time.sleep(0.5)
    '''
    udp_socket6.sendto(str(data).encode(), server_address6)
    time.sleep(0.5)          
    udp_socket7.sendto(str(data).encode(), server_address7) 
    time.sleep(0.5)
    udp_socket8.sendto(str(data).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(data).encode(), server_address9)    
    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(data).encode(), server_address10)

def aggregate_socket():
    print("Aggregation..!!!!")
    data = "aggregate"
    '''
    udp_socket.sendto(str(data).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(data).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(data).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(data).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(data).encode(), server_address5)   
    time.sleep(0.5) 
    '''     
    udp_socket6.sendto(str(data).encode(), server_address6)
    time.sleep(0.5)

    udp_socket7.sendto(str(data).encode(), server_address7)

    time.sleep(0.5)
    udp_socket8.sendto(str(data).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(data).encode(), server_address9)

    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(data).encode(), server_address10)


def home_socket(): 
    print("Home....******")
    data = "home"
    '''
    udp_socket.sendto(str(data).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(data).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(data).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(data).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(data).encode(), server_address5)
    time.sleep(0.5)
    '''
    udp_socket6.sendto(str(data).encode(), server_address6)
    time.sleep(0.5)
    udp_socket7.sendto(str(data).encode(), server_address7)     
    time.sleep(0.5)
    udp_socket8.sendto(str(data).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(data).encode(), server_address9)      
    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(data).encode(), server_address10)


def different_alt_socket(initial_alt,alt_diff):
    data =str(initial_alt)+str(",")+str(alt_diff)
    print(data)
    g="different"+","+str(data)
    print(g,"data")
    '''
    udp_socket.sendto(str(g).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(g).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(g).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(g).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(g).encode(), server_address5)
    time.sleep(0.5)
    '''

    udp_socket6.sendto(str(g).encode(), server_address6)
    time.sleep(0.5)

    udp_socket7.sendto(str(g).encode(), server_address7)

    time.sleep(0.5)
    udp_socket8.sendto(str(g).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(g).encode(), server_address9)

    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(g).encode(), server_address10)

def same_alt_socket(alt_same):
    print("Same_altitude")
    data = alt_same
    print(data,"data")
    f="same"+","+str(data)
    print(f,"f")
    '''
    udp_socket.sendto(str(f).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(f).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(f).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(f).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(f).encode(), server_address5)       
    time.sleep(0.5)
    '''
    udp_socket6.sendto(str(f).encode(), server_address6)
    time.sleep(0.5)      
    udp_socket7.sendto(str(f).encode(), server_address7)

    time.sleep(0.5)
    udp_socket8.sendto(str(f).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(f).encode(), server_address9)       
    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(f).encode(), server_address10)


def home_goto_socket(): 
    #udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = "home_goto"
    '''
    udp_socket.sendto(str(data).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(data).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(data).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(data).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(data).encode(), server_address5)      
    time.sleep(0.5)
    '''
    udp_socket6.sendto(str(data).encode(), server_address6)
    time.sleep(0.5)

    udp_socket7.sendto(str(data).encode(), server_address7)

    time.sleep(0.5)
    udp_socket8.sendto(str(data).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(data).encode(), server_address9)

    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(data).encode(), server_address10)

def rtl_socket():
    global socket,udp_socket,server_address1,server_address2,udp_socket2
    #udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = "rtl"
    '''
    udp_socket.sendto(str(data).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(data).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(data).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(data).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(data).encode(), server_address5)
    time.sleep(0.5)
    '''
    udp_socket6.sendto(str(data).encode(), server_address6)
    time.sleep(0.5)      
    udp_socket7.sendto(str(data).encode(), server_address7)       
    time.sleep(0.5)
    udp_socket8.sendto(str(data).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(data).encode(), server_address9)      
    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(data).encode(), server_address10)

def stop_socket():
    print("STOP>>>>>>>>>>>>")
    global socket1,udp_socket,udp_socket2,server_address1,server_address2      
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = "stop"
    '''
    socket1.sendto(str(data).encode(), server_address11)
    time.sleep(0.5)
    socket2.sendto(str(data).encode(), server_address12)
    time.sleep(0.5)
    '''
    socket3.sendto(str(data).encode(), server_address13)
    time.sleep(0.5)
    '''
    socket4.sendto(str(data).encode(), server_address14)
    time.sleep(0.5)
    '''
    socket5.sendto(str(data).encode(), server_address15)    
    time.sleep(0.5)
    '''
    socket6.sendto(str(data).encode(), server_address16)
    time.sleep(0.5)

    socket7.sendto(str(data).encode(), server_address17)

    time.sleep(0.5)
    socket8.sendto(str(data).encode(), server_address18)
    time.sleep(0.5)
    socket9.sendto(str(data).encode(), server_address19)      
    time.sleep(0.5)
    '''
    socket10.sendto(str(data).encode(), server_address20)

def return_socket():
    global socket,return_flag,udp_socket,server_address1,server_address2,udp_socket2
    #print("&&&&&")
    return_flag=True
    #udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = "return"
    '''
    udp_socket.sendto(str(data).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(data).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(data).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(data).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(data).encode(), server_address5)
    time.sleep(0.5)
    '''
    udp_socket6.sendto(str(data).encode(), server_address6)
    time.sleep(0.5)

    udp_socket7.sendto(str(data).encode(), server_address7)

    time.sleep(0.5)
    udp_socket8.sendto(str(data).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(data).encode(), server_address9)
    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(data).encode(), server_address10)

def specific_bot_goal_socket(drone_num,goal_num): 
    print("$$$##Specific_bot_goal###")
    d="specific_bot_goal"+","+str(drone_num)+","+str(goal_num)
    print("d",d)
    '''
    udp_socket.sendto(str(d).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(d).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(d).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(d).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(d).encode(), server_address5)
    time.sleep(0.5)
    '''
    udp_socket6.sendto(str(d).encode(), server_address6)
    time.sleep(0.5)

    udp_socket7.sendto(str(d).encode(), server_address7)

    time.sleep(0.5)
    udp_socket8.sendto(str(d).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(d).encode(), server_address9)
    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(d).encode(), server_address10)


def goal_socket(goal_num):     
    print("***Group goal*****!!!!!")
    d="goal"+","+str(goal_num)
    print("d",d)
    '''
    udp_socket.sendto(str(d).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(d).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(d).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(d).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(d).encode(), server_address5)
    time.sleep(0.5)
    '''
    udp_socket6.sendto(str(d).encode(), server_address6)
    time.sleep(0.5)

    udp_socket7.sendto(str(d).encode(), server_address7)

    time.sleep(0.5)
    udp_socket8.sendto(str(d).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(d).encode(), server_address9)
    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(d).encode(), server_address10)
    
def master(master_num):             
    global master_ip
    master_ip=master_num    
    data = "master" + "-" + str(master_num)
    print("data",data)
    '''
    socket1.sendto(str(data).encode(), server_address11)
    time.sleep(0.5)
    socket2.sendto(str(data).encode(), server_address12)
    time.sleep(0.5)
    '''
    socket3.sendto(str(data).encode(), server_address13)
    time.sleep(0.5)
    '''
    socket4.sendto(str(data).encode(), server_address14)
    time.sleep(0.5)
    '''
    socket5.sendto(str(data).encode(), server_address15)
    time.sleep(0.5)
    '''
    socket6.sendto(str(data).encode(), server_address16)
    time.sleep(0.5)

    socket7.sendto(str(data).encode(), server_address17)

    time.sleep(0.5)
    socket8.sendto(str(data).encode(), server_address18)
    time.sleep(0.5)
    socket9.sendto(str(data).encode(), server_address19)
    time.sleep(0.5)
    '''
    socket10.sendto(str(data).encode(), server_address20)

    if master==1:
        master_ip='192.168.29.151'
    elif master==2:
        master_ip='192.168.29.152'
    elif master==3:
        master_ip='192.168.29.153'
    elif master==4:
        master_ip='192.168.29.154'
    elif master==5:
        master_ip='192.168.29.155'
    elif master==6:
        master_ip='192.168.29.156'
    elif master==7:
        master_ip='192.168.29.157'
    elif master==8:
        master_ip='192.168.29.158'
    elif master==9:
        master_ip='192.168.29.159'
    elif master==10:
        master_ip='192.168.29.160'
        
    return True
    #mavlink_add()

def mavlink_add():
    global master_ip
    master_ip_array=['192.168.29.151','192.168.29.152','192.168.29.153','192.168.29.154','192.168.29.155','192.168.29.156','192.168.29.157','192.168.29.158','192.168.29.159','192.168.29.160']
    master_ip=master_ip_array[int(master)-1]
    print("master_ip",master_ip)
    add='output add '
    remove='output remove '

    port_array=[':14551',':14552',':14553',':14554',':14555',':14556',':14557',':14558',':14559',':14560']


    data=add+master_ip
    #data=remove+master_ip
    print("data",(data+port_array[0]),type(data))	
    '''
    mavlink_sock1.sendto((data+port_array[0]).encode(), mavlink_server_address1)
    time.sleep(0.5)
    mavlink_sock2.sendto((data+port_array[1]).encode(), mavlink_server_address2)
    time.sleep(0.5)
    '''
    mavlink_sock3.sendto((data+port_array[2]).encode(), mavlink_server_address3)
    time.sleep(0.5)
    '''
    mavlink_sock4.sendto((data+port_array[3]).encode(), mavlink_server_address4)
    time.sleep(0.5)
    '''
    mavlink_sock5.sendto((data+port_array[4]).encode(), mavlink_server_address5)
    time.sleep(0.5)
    '''
    mavlink_sock6.sendto((data+port_array[5]).encode(), mavlink_server_address6)
    time.sleep(0.5)

    mavlink_sock7.sendto((data+port_array[6]).encode(), mavlink_server_address7)

    time.sleep(0.5)
    mavlink_sock8.sendto((data+port_array[7]).encode(), mavlink_server_address8)
    time.sleep(0.5)
    mavlink_sock9.sendto((data+port_array[8]).encode(), mavlink_server_address9)
    time.sleep(0.5)
    '''
    mavlink_sock10.sendto((data+port_array[9]).encode(), mavlink_server_address10)

def mavlink_remove(remove_link):
    global master_ip
    #data = removelink_entry.get()
    master_ip_array=['192.168.29.151','192.168.29.152','192.168.29.153','192.168.29.154','192.168.29.155','192.168.29.156','192.168.29.157','192.168.29.158','192.168.29.159','192.168.29.160']
    master_ip=master_ip_array[int(remove_link)-1]
    print("master_ip",master_ip)
    add='output add '
    remove='output remove '
    port_array=[':14551',':14552',':14553',':14554',':14555',':14556',':14557',':14558',':14559',':14560']
    data=remove+master_ip
    print("data",(data+port_array[0]),type(data))
    '''
    mavlink_sock1.sendto((data+port_array[0]).encode(), mavlink_server_address1)
    time.sleep(0.5)
    mavlink_sock2.sendto((data+port_array[1]).encode(), mavlink_server_address2)
    time.sleep(0.5)
    '''
    mavlink_sock3.sendto((data+port_array[2]).encode(), mavlink_server_address3)
    time.sleep(0.5)
    '''
    mavlink_sock4.sendto((data+port_array[3]).encode(), mavlink_server_address4)
    time.sleep(0.5)
    '''
    mavlink_sock5.sendto((data+port_array[4]).encode(), mavlink_server_address5)
    time.sleep(0.5)
    '''
    mavlink_sock6.sendto((data+port_array[5]).encode(), mavlink_server_address6)
    time.sleep(0.5)
        
    mavlink_sock7.sendto((data+port_array[6]).encode(), mavlink_server_address7)

    time.sleep(0.5)
    mavlink_sock8.sendto((data+port_array[7]).encode(), mavlink_server_address8)
    time.sleep(0.5)
    mavlink_sock9.sendto((data+port_array[8]).encode(), mavlink_server_address9)
    time.sleep(0.5)
    '''
    mavlink_sock10.sendto((data+port_array[9]).encode(), mavlink_server_address10)

def bot_remove(remove_uav_num):
    print("!!!bot_remove!!")
    
    data = "remove_bot"+","+str(remove_uav_num)
    print("remove_link_num",remove_uav_num)
    '''
    udp_socket.sendto(str(data).encode(), server_address1)
    time.sleep(0.5)
    udp_socket2.sendto(str(data).encode(), server_address2)
    time.sleep(0.5)
    '''
    udp_socket3.sendto(str(data).encode(), server_address3)
    time.sleep(0.5)
    '''
    udp_socket4.sendto(str(data).encode(), server_address4)
    time.sleep(0.5)
    '''
    udp_socket5.sendto(str(data).encode(), server_address5)
    time.sleep(0.5)
    '''
    udp_socket6.sendto(str(data).encode(), server_address6)
    time.sleep(0.5)

    udp_socket7.sendto(str(data).encode(), server_address7)

    time.sleep(0.5)
    udp_socket8.sendto(str(data).encode(), server_address8)
    time.sleep(0.5)
    udp_socket9.sendto(str(data).encode(), server_address9)
    time.sleep(0.5)
    '''
    udp_socket10.sendto(str(data).encode(), server_address10)

