import socket
import threading
import sys
import signal
import os

SERVER= socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the server socket to the address
client.connect(ADDR)


# this function handles the client connection
def receive():
    try:
        while True:
            while True:
                message=client.recv(1024).decode('utf-8')
                if message:
                    break
            print(message)
    except:
        print("client is closed")
        client.close()
        pid = os.getpid()
        os.kill(pid, signal.SIGINT)
    

def send():
    try:
        while True:
            message = input()
            if(message=='x'):
                client.send("DISCONNECT".encode('utf-8'))
                client.close()
                break
            client.send(message.encode('utf-8'))
    except:
        print("client is closed")
        client.close()
        pid = os.getpid()
        os.kill(pid, signal.SIGINT)

threading.Thread(target=receive).start()
threading.Thread(target=send).start()
