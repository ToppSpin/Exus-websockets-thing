import socket            
s = socket.socket()        
port = 6666

s.connect(('78.71.14.72', port))
newPort = int(s.recv(1024).decode())
s.close()

s = socket.socket()

s.connect(('78.71.14.72', newPort))
while True:
    x = input("Write here: ")
    s.send(x.encode())
    print('>> ', s.recv(1024).decode())