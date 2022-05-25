
# ----- An UDP client in Python that sends temperature values to server-----

import socket
from datetime import datetime
import random
import time
 


# Get temperature


start_file = f'client_log_{datetime.utcnow()}.log'

# A tuple with server ip and port
def send(ip_address,port_address,mesaage,start_file):
    serverAddress = (ip_address, port_address);

    
    
# Create a datagram socket

    tempSensorSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);

 

# Get temperature


 

# Socket is not in connected state yet...sendto() can be used

# Send temperature to the server

    tempSensorSocket.sendto(mesaage.encode(), (ip_address,port_address));

 

# Read UDP server's response datagram

    response = tempSensorSocket.recv(1024);
    with open(start_file, 'a') as f:
        print (response)
        f.write(f"{datetime.utcnow()} {mesaage}")


def main():
    
    ip_address = input("what is your ip address : ")
    port_number = int(input("what is your port number : "))
    delay = float(input("how lond is your dilay : "))
    
    file1 = open('data.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        time.sleep(delay)
        send(ip_address,port_number,line,start_file)

if __name__ == "__main__":
    main()