import socket
import threading
from Encryptor import Encryptor
from Decryptor import Decryptor
from utils import *

    
# Connect to the server
SERVER= socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the server socket to the address
client.connect(ADDR)

# Get the client name
name=input("Enter your name: ")
client.send(name.encode('utf-8'))

# Create the encryptor object
encryptor=Encryptor(170,200)

# Get the public key
n,e=encryptor.get_public_key()

# Get the private key
d=encryptor.get_private_key()

# Send the public key to the server
client.send((str(n)+','+str(e)).encode('utf-8'))

#Get the other client name
other_name=client.recv(1<<20).decode('utf-8')

# Get the other client's public key
public_key = client.recv(1<<20).decode('utf-8').split(',')
public_n = int(public_key[0])
public_e = int(public_key[1])
encryptor.set_other_party_public_key(public_n,public_e)
print("the other client public key is: ",public_key)


# Create Decryptor object
decryptor=Decryptor(n,d)



# this function handles the client connection
def receive():
    while True:
        # Receive the encrypted message
        encrypted_message=client.recv(1<<20).decode('utf-8')

        # Decrypt and decode the message
        message=decryptor.decrypt_and_decode(encrypted_message)
        
        # Print the message
        print(f'{other_name}:{message}')

def send():
    while True:
        # Get the message from the user
        message = input()
        message=message.lower()

        # Terminate the connection if the user enter x
        if(message=='x'):
            client.send("DISCONNECT".encode('utf-8'))
            client.close()
            break
        message_encrypted=encryptor.encrypt_and_encode(message)
        client.send(message_encrypted.encode('utf-8'))


threading.Thread(target=receive).start()
threading.Thread(target=send).start()
