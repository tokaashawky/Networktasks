from socket import *
from _thread import *
s=socket(AF_INET,SOCK_STREAM)
host='127.0.0.1'
port=7050
s.connect((host,port))
alias=input("Enter your alias? ")
def recv_fun():
    while True:
        try:
            msg=s.recv(2048).decode('utf-8')
            if msg== 'alias?':
                s.send(alias.encode('utf-8'))
            else:
                print(f"{alias}: ",msg)
        except:
            print("you left")
            s.close()
            break

def send_fun():
     while True:
        x=input("")
        msg=f"{alias}: {x}".encode('utf-8')
        s.send(msg)
        if x== "bye":
            s.close()
            break



start_new_thread(recv_fun,(s,))
start_new_thread(send_fun,(s,))