import socket       
import threading as th

s = socket.socket()        
port = 6666
<<<<<<< HEAD
host = '78.71.14.72'
=======
host = '192.168.165.65'
>>>>>>> ce3536627b53f573079036f561b149184ab9e5d3

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