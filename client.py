import socket            
s = socket.socket()        
port = 6666

s.connect(('78.71.14.72', port))

while True:
    x = input("")
    s.send(x.encode())
    print(s.recv(1024).decode())

