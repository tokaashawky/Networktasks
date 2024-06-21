from socket import *
from _thread import *
def receive_theard(s):
    while True:
        print(f"Server: {s.recv(2048).decode('utf-8')}")
s=socket(AF_INET,SOCK_STREAM)
host='127.0.0.1'
port=7050
s.connect((host,port))
start_new_thread(receive_theard,(s,))
while True:
    s.send(input("Client: ").encode('utf-8'))
s.close()
