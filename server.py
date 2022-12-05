import socket
import multiprocessing as mp

def con(Connection, adress):
    

connections = {}

s = socket.socket()
port = 6666
s.bind(('', port))

while True:
    s.listen(5)
    c, addr = s.accept()
    print ('Got connection from', addr)

    while True:
        print(">> ", c.recv(1024).decode())
        c.send("2".encode())