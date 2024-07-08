# importing the module
import socket

client_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 5555 
client_object.connect((ip_address, port))
data_received = client_object.recv(1024)

if data_received:
    print(f"Data received from server: {data_received.decode()}")
    while data_received:
        msg = input("Client: ")
        client_object.send(msg.encode())
        data_received = client_object.recv(1024)
        if data_received:
            print(f"Data received from server: {data_received.decode()}")
