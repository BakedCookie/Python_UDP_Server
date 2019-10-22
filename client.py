#!/usr/bin/python

import socket
import random

def makeList():
    message = []
    for i in range(10):
        message.append(random.randint(0,10))
    return message

for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    message_org = makeList()
    message = bytearray(message_org)
    addr = ("127.0.0.1", 22222)
    client_socket.sendto(message, addr)
    try:
        data, server = client_socket.recvfrom(1024)
        print(list(data))
        print(message_org)
    except socket.timeout:
        print('REQUEST TIMED OUT')
