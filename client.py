import socket
import threading
import sys
import signal
import os
print("arguements are: ", sys.argv)
p=int(sys.argv[1])
q=int(sys.argv[2])
e=int(sys.argv[3])
n=p*q
fai = (p-1)*(q-1)

def gcd(a,b,x,y):
    if(a==0):
        return (0,1,b)
    else:
        x_prev,y_prev,gcd_val=gcd(b%a,a,x,y)
        x=y_prev-(b//a)*x_prev
        y=x_prev
        return (x,y,gcd_val)


def modinv(a,m):
    x,y,gcd_val=gcd(a,m,0,0)
    if(gcd_val!=1):
        return -1
    else:
        return (x%m+m)%m


d = modinv(e,fai)
print("d is: ",d,gcd(2,5,1,1))

def encrypt(plain_text):
    cipher_text=(plain_text**e)%n
    return cipher_text
def decrypt(cipher_text):
    plain_text=(cipher_text**d)%n
    return plain_text
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
    return result

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
            message=decrypt(int(message))
            message=decoder(message)
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
        message=str(encrypt(message))
        client.send(message.encode('utf-8'))

threading.Thread(target=receive).start()
threading.Thread(target=send).start()
