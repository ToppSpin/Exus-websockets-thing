import socket       
import threading as th

s = socket.socket()        
port = 6666
host = '192.168.165.65'

def clientR(c):
    while True:
        msg = c.recv(2048).decode()
        print(msg)

s.connect((host, port))

p1 = th.Thread(target=clientR, args=(s,))
p1.start()

while True:
    x = input("")
    s.send(x.encode())