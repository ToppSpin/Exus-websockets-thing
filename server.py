import socket
import threading as th

def newClient(c, addr):
    x = str(addr) + "din mamma"
    sender(x, addr)
    while True:
        msg = c.recv().decode()
        sender(msg, addr)

#Sender function sends the message to all clients except the sender
def sender(msg, addr): 
    for i in connections.items():
        if i[0] == addr:
            continue
        i[1].send(msg.encode())

#The needed variables
Threads = {}
connections = {}
serversocket = socket.socket()         
host = socket.gethostname() 
port = 6666
i = 0
        
print('Server started!')

serversocket.bind((host, port))        
serversocket.listen(5)                 

#The server will accept new clients and start a new thread for each client
while True:
    c, addr = serversocket.accept()
    print('Got connection from', addr)
    connections.update({i: c})
    Threads.update({i: th.Thread(target=newClient, args=(c, i,))})
    Threads[i].start()
    i =+ 1