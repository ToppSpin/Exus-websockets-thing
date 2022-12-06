import socket            
s = socket.socket()        
port = 6666

s.connect(('192.168.165.65', port))

while True:
    x = input("Write here: ")
    s.send(x.encode())
    print('>> ', s.recv(1024).decode())