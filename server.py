#!/usr/bin/python           # This is server.py file                                                                                                                                                                           

import socket               # Import socket module
import threading as th

Threads = {}
connections = {}
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 6666
i = 0

def newClient(c, addr):
    x = str(addr) + "din mamma"
    sender(x, addr)
    while True:
        msg = c.recv(123456789).decode()
        sender(msg, addr)
        

def sender(msg, addr): 
    for i in connections.items():
        if i[0] == addr:
            continue
        i[1].send(msg.encode())

print('Server started!')
print('Waiting for clients...')

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.


while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    connections.update({i: c})
    Threads.update({i: th.Thread(target=newClient, args=(c, i,))})
    Threads[i].start()
    i =+ 1


   
