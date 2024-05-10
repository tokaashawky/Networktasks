import threading
from socket import *
s = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 8000
s.bind((host, port))
s.listen()
clients = []
aliases = []

connect_client = 0 
def broadcast(msg, sender):
    for client in clients:
        if client != sender: 
            client.send(msg)

def handle_client(client):
    global connect_client  
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg, client)  
        except:
            ind = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[ind]
            broadcast(f'{alias} left chat room ^_^'.encode('utf-8'), client)  
            aliases.remove(alias)
            
            connect_client -= 1
            if connect_client == 0:
                s.close() 
            break

def receive():
    global connect_client 
    while True:
        print("server listening...")
        print("input 'close' if you want to leave chat ^_^ ")
        client, addr = s.accept()
        connect_client += 1  
        
        print(f'client {str(addr)} enter chat room ')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        
        print(f'the nickname of the client is: {alias}'.encode('utf-8'))
        broadcast(f'{alias} connected to the chat room'.encode('utf-8'), client)  # Pass sender client to broadcast
        client.send('you are connected ^_^'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()