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

def encoder(message):
    result= 0
    for (i,c) in enumerate(message):
        if(c>='0' and c<='9'):
            val=ord(c)-ord('0')
        elif(c>='a' and c<='z'):
            val=ord(c)-ord('a')+10
        else:
            val=36
        result+=val*(37**i)
    return str(result)

def decoder(message):
    result=""
    while(message>0):
        val=message%37
        if(val>=0 and val<=9):
            result+=chr(val+ord('0'))
        elif(val>=10 and val<=35):
            result+=chr(val+ord('a')-10)
        else:
            result+=' '
        message=message//37
    return result


# this function handles the client connection
def receive():
    try:
        while True:
            while True:
                message=client.recv(1024).decode('utf-8')
                if message:
                    break
            message=decoder(int(message))
            print(f'He:{message}')
    except:
        print("client is closed")
        client.close()
        pid = os.getpid()
        os.kill(pid, signal.SIGINT)
    

def send():
    while True:
        message = input()
        if(message=='x'):
            client.send("DISCONNECT".encode('utf-8'))
            client.close()
            break
        message=encoder(message)
        client.send(message.encode('utf-8'))

threading.Thread(target=receive).start()
threading.Thread(target=send).start()
