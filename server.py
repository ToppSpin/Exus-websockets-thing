import socket
s = socket.socket()
port = 6666
sg = socket.socket()
s.bind(('', port))
sg.bind(('', 9999))
s.listen(5)
c, addr = s.accept()
print ('Got connection from', addr)

while True:
    print(">> ", c.recv(1024).decode())
    c.send("2".encode())