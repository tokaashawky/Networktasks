from socket import *
s=socket(AF_INET,SOCK_STREAM)
host='127.0.0.1'
port=4000
s.bind((host,port))
s.listen(5)
print("server is listening :) ")
conn,add=s.accept()
print(f"client {add[0]} is connected :)")
while True:
    p=conn.recv(2048).decode('utf-8')
    print(f"Client: {p}" )
    if p == "bye":
        break
    msg=input("Server: ").encode('utf-8')
    len_msg=len(msg)
    if len_msg >2048:
        chunks= len_msg //2048 +1
        for x in range(chunks):
            start= x*2048
            end=min((1+x)*2048,len_msg)
            conn.send(msg[start:end])
    else:
        conn.send(msg)

conn.close()