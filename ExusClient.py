import socket

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 512)
s.connect(('192.168.2.253', 6666))

while True:
    x = input('Send msg: ')
    s.send(x.encode())