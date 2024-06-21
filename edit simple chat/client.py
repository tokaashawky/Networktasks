#divide msg into chunks
#print bye if you want to end chat

from socket import *
s=socket(AF_INET,SOCK_STREAM)
host= '127.0.0.1'
port= 4000
s.connect((host,port))
print("you are connected :)")
while True:
    msg = input("client: ").encode('utf-8')
    len_msg = len(msg)
    if len_msg > 2048:
        chunks = len_msg // 2048 + 1
        for i in range(chunks):
            start = i * 2048
            end = min((i + 1) * 2048, len_msg)
            s.send(msg[start:end])

    else:
        s.send(msg)
    if msg == "bye":
        break
    k=s.recv(2048).decode('utf-8')
    print(f"server : {k}")

s.close()