#!/usr/bin/python

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 22222))

print("Hello clients, send your array of integers of any dimension to UDP Server Port No 22222")

while True:
    message, address = server_socket.recvfrom(1024)

    message = list(message)
    message = [min(message),max(message)]

    message = bytearray(message)
    server_socket.sendto(message, address)
