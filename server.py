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

client1 = []
client2 = []


# this function handles the client connection
def handle_client(conn, addr):
    tid = threading.current_thread().ident
    print("thread id", tid)
    while True:
        message = conn.recv(5).decode('utf-8')
        if message:
            print(message)
            if message == 'DISCONNECT':
                conn.close()
                break


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(
            f'[CLIENT NUMBER {threading.active_count() - 1} IS CONNECTED]')


# to handle the ctrl+c
def signal_handler(signal, frame):
    print('Server is closing...')
    server.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

threading.Thread(target=start).start()
pid = os.getpid()
while True:
    exit=input()
    if(exit=='x'):
        os.kill(pid, signal.SIGINT)
