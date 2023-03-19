import socket
import threading
import sys
import signal

SERVER= socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the server socket to the address
client.connect(ADDR)


# this function handles the client connection
def receive():
    while True:
        while True:
            message=client.recv(1024).decode('utf-8')
            if message:
                break
        print(message)

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

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    client.send("DISCONNECT".encode('utf-8'))
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)