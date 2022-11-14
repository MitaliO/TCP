import socket
import subprocess
import json
import time
import base64
# import requests
import ctypes
import sys


def reliable_send(data):
    json_data = json.dumps(data)
    socket.send(json_data)


def reliable_receive():
    json_data =" "
    while True:
        try:
            json_data = json_data + socket.receive(1024)
            return json.loads(json_data)
        except ValueError:
            continue


def connection():
    socket.connect(("10.10.10.2",8080))
    shell()


def shell():
    n = len(sys.argv)
    string = ''
    for i in range(1,n):
        string+=str(sys.argv[i]) + " "

    reliable_send(string)
    print("Sent:" + string)
    count_digits = reliable_receive()
    print("Received: "+ count_digits)
