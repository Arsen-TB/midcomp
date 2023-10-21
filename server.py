#echo-sarvar.py

import socket 
import time
#import pandas as pd

HOST = "127.0.0.1"
PORT = 12345

reply_message = "success"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) 
    s.listen() # here in brackets you can define how many times can it listen until client connects
    conn, addr = s.accept()  #so this is accepting the connection and the address and s.accept() is used to connect to the server
    with conn:
        print(f"Connected by {addr}")
        while True:
            time.sleep(1)
            data = conn.recv(1024) # so basically socket.recv(buffer_size) will receive data with every time receiving 1024 bytes as buffersize is like that

            if not data:
                print("client is gone")
                break

            print(f"received: {data} ; from {addr} ")
            conn.sendall(reply_message.encode())

