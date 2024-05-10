import threading
from socket import *
alias = input('input yout alias: ')
client = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 8000
client.connect((host,port))
def clientrecv():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(msg)
        except:
            print(" you left chat room.")
            client.close()
            break
def clientsend():
    while True:
        x = input("")
        msg = f'{alias}: {x}'
        client.send(msg.encode('utf-8'))
        if x == "close" :
            client.close()
            break
recv_thread = threading.Thread(target=clientrecv)
recv_thread.start()
send_thread = threading.Thread(target=clientsend)
send_thread.start()