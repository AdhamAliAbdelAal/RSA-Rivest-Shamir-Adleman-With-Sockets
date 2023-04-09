import socket
import threading
import sys
import signal
import os
from utils import *
from sympy import randprime

# Generate the public and private keys
p=randprime(10**50,10**60)
q=randprime(10**50,10**60)
# Make sure that p and q are different
while(p==q):
    q=randprime(10**50,10**60)
n=p*q
fai = (p-1)*(q-1)
# Choose e such that it is coprime with fai and less than fai gcd(x,x-1) is always 1
e=fai-1
# Calculate the private key
d = modinv(e,fai)
    
# Connect to the server
SERVER= socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the server socket to the address
client.connect(ADDR)


# Send the public key to the server
client.send((str(n)+','+str(e)).encode('utf-8'))


# Get the other client's public key
public_key = client.recv(1024).decode('utf-8').split(',')
public_n = int(public_key[0])
public_e = int(public_key[1])
print("the other client public key is: ",public_key)



# this function handles the client connection
def receive():
    while True:
        # Receive the encrypted message
        encrypted_message=client.recv(1024).decode('utf-8')

        # Get the number of sets of 5 characters
        encrypted_message=encrypted_message.split(' ')
        message_sets_len=len(encrypted_message)
        message=''
        for i in range(message_sets_len):
            decrypted_block=decrypt(int(encrypted_message[i]),d,n)
            message+=decoder(decrypted_block)    
        
        print(f'He:{message}')

def send():
    while True:
        # Get the message from the user
        message = input()

        # Terminate the connection if the user enter x
        if(message=='x'):
            client.send("DISCONNECT".encode('utf-8'))
            client.close()
            break

        # Append spaces to the message to make it a multiple of 5
        message_len=len(message)
        if(message_len%5!=0):
            message+=' '*(5-message_len%5)
            message_len+=(5-message_len%5)
        message_encrypted=[]
        for i in range(0,message_len,5):
            message_encoded=encoder(message[i:i+5])
            message_encrypted.append(str(encrypt(message_encoded,public_e,public_n)))
        message_encrypted=' '.join(message_encrypted)
        client.send(message_encrypted.encode('utf-8'))


threading.Thread(target=receive).start()
threading.Thread(target=send).start()
