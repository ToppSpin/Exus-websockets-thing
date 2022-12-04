#!/usr/bin/python           # This is server.py file                                                                                                                                                                           
import random
import socket               # Import socket module
import multiprocessing as mp
# Function describing multiprocess (Class maybe)
def server(port):
    temp_server = socket.socket()
    temp_server.bind(('', port))
    temp_server.listen(5)
    connection, addr = temp_server.accept()
    print ('Got connection from', addr)
    try:
        while True:
            print('>> ', connection.recv(1024).decode())
            x = input("Write here: ")
            connection.send(x.encode())
    except:
        del servers[port] 


def returnPort():
    while True:
        aPort = random.randint(6667, 7000)
        if aPort not in servers:
            servers.update({aPort: mp.Process(target=server, args=(aPort,))})
            return aPort

global servers
servers = {}

if __name__ == '__main__':
    while True:
        s = socket.socket()
        s.bind(('', (6666)))
        print("Hej")
        s.listen(5)
        print("hejda")
        c, addr = s.accept()
        print("HEj")
        print ('Got connection from', addr)
        sendPort = returnPort()
        servers[sendPort].start()
        c.send(str(sendPort).encode())
        c.close()
        s.close()

# Multiprocess starter and storage