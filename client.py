import socket
import threading
import time

SERVER= socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the server socket to the address
client.connect(ADDR)


# this function handles the client connection
def receive():
    print("receive!!!!")

def send():
    while True:
        message = input()
        if(message=='x'):
            client.send("DISCONNECT".encode('utf-8'))
            client.close()
            break
        client.send(message.encode('utf-8'))

threading.Thread(target=receive).start()
threading.Thread(target=send).start()