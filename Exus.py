import socket
import threading
import time

s = socket.socket()
port = 6666

s.bind(('', port))

s.listen(5)

c, addr = s.accept()
print('Got a connection from:', addr)





while True:
    x = input("YEs")
    c.send(x.encode())