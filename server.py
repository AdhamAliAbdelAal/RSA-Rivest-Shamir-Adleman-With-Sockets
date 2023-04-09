import socket
import threading
import sys
import signal
import os


# this is the ip address of the server
# socket.gethostbyname(socket.gethostname()) is the ip address of the server
# socket.gethostname() is the name of the server
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)

# this is the server socket
# socket.AF_INET is the address family of the socket
# socket.SOCK_STREAM is the socket type
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the server socket to the address
server.bind(ADDR)

clients_conns = [None]*2
keys = [None]*2

# this function handles the client connection


def handle_client(conn, addr):
    me = threading.active_count()-3
    clients_conns[me] = conn
    you = 1-me

    # receive the public key from the client
    key = conn.recv(1024).decode('utf-8')
    keys[me]=key
    
    # if all clients are connected, send the public keys to each other
    if(me==1):
        clients_conns[me].send(keys[you].encode('utf-8'))
        clients_conns[you].send(keys[me].encode('utf-8'))

    # receive the messages from the clients
    while True:
        message = conn.recv(1024).decode('utf-8')
        if message == 'DISCONNECT':
            conn.close()
            break
        clients_conns[you].send(message.encode('utf-8'))


def start():
    server.listen(2)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(
            f'[CLIENT NUMBER {threading.active_count() - 2} IS CONNECTED]')


threading.Thread(target=start).start()

# terminate server
pid = os.getpid()
while True:
    exit=input()
    if(exit=='x'):
        os.kill(pid, signal.SIGINT)
