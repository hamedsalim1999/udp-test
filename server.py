import socket

import datetime


ip_address = input("what is your ip address : ")
port_number = int(input("what is your port number : "))
 

# Define the IP address and the Port Number


listeningAddress = (ip_address, port_number)

 
# Create a datagram based server socket that uses IPv4 addressing scheme

datagramSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

datagramSocket.bind(listeningAddress)
 
while(True):

    tempVal, sourceAddress = datagramSocket.recvfrom(128)
    with open("server_log.log", "a") as file_object:
        file_object.write(f"{datetime.datetime.utcnow()} Temperature at {sourceAddress} is {tempVal.decode()}  \n")

    response = f"Received at: {datetime.datetime.utcnow()}"

    # datagramSocket.sendto(response.encode(), sourceAddress)