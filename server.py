import socket
s = socket.socket()
port = 6666

s.bind(('', port))

s.listen(5)
c, addr = s.accept()
print ('Got connection from', addr)

while True:
    print(c.recv(1024).decode())
    x = input("")
    c.send(x.encode())