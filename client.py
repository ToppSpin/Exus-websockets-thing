import socket       
import threading as th

#The client will split into two processes, one for sending and one for recieving

#The recieving process
def clientR(connection):
    while True:
        message = connection.recv(2048).decode()
        print(message)

#The needed variables
Clientsocket = socket.socket()        
port = 6666
host = '10.189.37.0'

#The socket connects and starts the recieving process
Clientsocket.connect((host, port))
procces1 = th.Thread(target=clientR, args=(Clientsocket,))
procces1.start()

#After that the sending process starts
while True:
    x = input("")
    Clientsocket.send(x.encode())