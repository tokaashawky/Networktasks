from socket import *
s = socket(AF_INET,SOCK_STREAM)
print("socket successfully created")
host='127.0.0.1'
port= 8000
s.bind((host,port))
print("socket bind at: ",port)
s.listen(5)
print("socket is listening ^_^")
c,addr = s.accept()
print('get connection from: ', addr)

while True:
    x=c.recv(2048)
    print("client:",x.decode('utf-8'))
    if x.decode('utf-8') == "end" :
        break
    msg= input("server: ").encode('utf-8')
    msg_length = len(msg)
    if msg_length > 2048:
        chunks = msg_length // 2048 + 1
        for i in range(chunks):
            start = i * 2048
            end = min((i + 1) * 2048, msg_length)
            s.send(msg[start:end])
    else:
        c.send(msg)
c.close()