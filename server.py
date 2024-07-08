# Importing the necessary libraries
import socket 

# Creating a socket object
server_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

#  connecting to local host
ip_address = "127.0.0.1"
port = 5555
server_object.bind((ip_address, port))
server_object.listen(1)

connection_object, address = server_object.accept()

if connection_object:
    print("Connection from " + str(address) + " has been established.")
    msg = "Hello " + str(address) + "!"
    connection_object.send(msg.encode())
    data_received = connection_object.recv(1024)

    while data_received != b"quit":
        print("Client: " + data_received.decode())
        msg = input("Server: ")
        connection_object.send(msg.encode())
        data_received = connection_object.recv(1024)