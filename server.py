import socket
import multiprocessing as mp

def con(Connection):
    print("yoyo")
    while True:
        print(">> ", Connection.recv(1024).decode())
        Connection.send("2".encode())

connections = {}

s = socket.socket()
port = 6666
i = 0

if __name__ == '__main__':
    while True:
        s.bind(('', port))
        s.listen(5)
        c, addr = s.accept()
        print ('Got connection from', addr)
        connections.update({i:mp.Process(target=con, args=(c,))})
        connections[i].start()
        i += 1
        port = port + 1