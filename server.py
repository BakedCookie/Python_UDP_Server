#!/usr/bin/python
import socket

# Loop back IP, used for testing
serverIP = 'localhost'
serverPort = 22222
bufferSize = 2048

"""create a server socket object,
typically takes 2 params, 1st defines IP type, 2nd is for protocol (UDP)"""
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind object to the address we created
serverSocket.bind((serverIP, serverPort))

# debug message
print("Hello clients, send your array of integers of any dimension to UDP Server Port No 22222")

# infinite loop
while True:
    # listening for packets send from client
    clientData, clientAdd = serverSocket.recvfrom(bufferSize)
    # convert byte message back to array of ints
    clientData = list(clientData)
    clientData = [min(clientData), max(clientData)]
    # convert message to byte message
    clientData = bytearray(clientData)
    # Send response to client
    serverSocket.sendto(clientData, clientAdd)

