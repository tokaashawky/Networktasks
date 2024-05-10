from socket import *
s = socket(AF_INET,SOCK_STREAM)
host='127.0.0.1'
port= 8000
s.connect((host,port))
print("input 'close' if you want to close chat ")
while True:
    msg= input("client: ").encode('utf-8')
    msg_length = len(msg)
    if msg_length > 2048:
        chunks = msg_length // 2048 + 1
        for i in range(chunks):
            start = i * 2048
            end = min((i + 1) * 2048, msg_length)
            s.send(msg[start:end])
    else:
        s.send(msg)
    if msg.decode('utf-8') == "close" :
         break
    x=s.recv(2048)
    print("server:",x.decode('utf-8'))
s.close()