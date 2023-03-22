import socket
import threading
import sys
import signal
import os
from utils import *
print("arguements are: ", sys.argv)
p=int(sys.argv[1])
q=int(sys.argv[2])
n=p*q
e=n-2
fai = (p-1)*(q-1)
d = modinv(e,fai)
print("d is: ",d)




    
SERVER= socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the server socket to the address
client.connect(ADDR)

# Send the public key to the server
client.send((str(n)+','+str(e)).encode('utf-8'))

# Get the other client's public key
while True:
    public_key = client.recv(1024).decode('utf-8').split(',')
    if public_key:
        public_n = int(public_key[0])
        public_e = int(public_key[1])
        print("the other client public key is: ",public_key)
        break


# this function handles the client connection
def receive():
    while True:
            while True:
                message=client.recv(1024).decode('utf-8')
                if message:
                    break
            message=decrypt(int(message),d,n)
            message=decoder(message)
            print(f'He:{message}')

def send():
    while True:
        message = input()
        if(message=='x'):
            client.send("DISCONNECT".encode('utf-8'))
            client.close()
            break
        message=encoder(message)
        message=str(encrypt(message,public_e,public_n))
        client.send(message.encode('utf-8'))


threading.Thread(target=receive).start()
threading.Thread(target=send).start()
