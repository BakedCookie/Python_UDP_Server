#!/usr/bin/python
import socket
import random

serverIP = 'localHost'
serverPort = 22222
bufferSize = 2048


def makeList():
    message = []
    for i in range(random.randint(5, 20)):
        message.append(random.randint(0, 10))
    return message


# Create a socket object for the client
# AF_INET indicates IPv4 network, SOCK_DGRAM indicates UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create, encode and send message
message_org = makeList()
clientMessage = bytearray(message_org)
clientSocket.sendto(clientMessage, (serverIP, serverPort))

# We receive two parts
serverData, serverAdd = clientSocket.recvfrom(bufferSize)

print("Received new data from server")
# Decode
serverData = list(serverData)
# Print to terminal
print("From "+str(serverAdd[0])+" at "+str(serverAdd[1])+":")
print("Min:"+str(serverData[0])+", Max:"+str(serverData[1]))

clientSocket.close()

