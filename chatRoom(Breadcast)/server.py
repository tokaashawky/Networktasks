from socket import *
from _thread import *

s=socket(AF_INET,SOCK_STREAM)
host='127.0.0.1'
port=7050
s.bind((host,port))
s.listen()
print("server is listening ")
clients = []
aliases = []

clients_connected=0
def broadcast(msg,conn):
    for client in clients:
        if client != conn:
            client.send(msg)
def handle_client(conn):
    global clients_connected
    while True:
        try:
            msg=conn.recv(2048).decode('utf-8')
            broadcast(msg,conn)
        except:
            index=clients.index[conn]
            clients.remove(conn)
            conn.close()
            alias=aliases[index]
            broadcast(f"{alias} left chat room ",conn)
            aliases.remove(alias)

            clients_connected -=1
            if clients_connected==0:
                s.close()
def receive():
    global clients_connected
    while True:
        conn,add=s.accept()
        clients_connected += 1
        conn.send('alias?'.encode('utf-8'))
        alias=conn.recv(2048).decode
        clients.append(conn)
        aliases.append(alias)
        print( f"{alias} is connected chat room :)")
        conn.send('Welcome you are enter chat room ^_^'.encode('utf-8'))
        broadcast(f"{alias} enter chat room..".encode('utf-8'),conn)
        start_new_thread(handle_client,conn)

if __name__ == "__main__":
    receive()
