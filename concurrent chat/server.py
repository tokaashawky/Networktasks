from socket import *
from _thread import *
def send_tread(conn):
    start_new_thread(recv_thread,(conn,))
    while True:
        conn.send(input("server: ").encode('utf-8'))

def recv_thread(conn):
    while True:
        print(f"Client: {conn.recv(2048).decode('utf-8')}")
s=socket(AF_INET,SOCK_STREAM)
host='127.0.0.1'
port=7050
s.bind((host,port))
s.listen(5)
print("server is listening ")
while True:
    conn,add=s.accept()
    print(f"client of ip: {add[0]} and port: {add[1]} connected ")
    start_new_thread(send_tread,(conn,))
conn.close()