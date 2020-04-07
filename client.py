from socket import * 
from threading import Thread


s = socket(AF_INET , SOCK_STREAM)
s.setsockopt(SOL_SOCKET , SO_REUSEADDR , 1)

HOST = '127.0.0.1'
PORT = 7788
s.connect((HOST , PORT))
BUFF_SIZE = 1024    


msg = s.recv(BUFF_SIZE).decode("utf-8") # receive welcome message 

print(msg)

name = input("Enter your name : ")
name = name.encode("utf-8")

s.send(name) # send name 

msg = s.recv(BUFF_SIZE).decode("utf-8") # receive  second welcome message 
print(msg)

def clientSend():
    try:
        while 1 :
            msg = input('me:- ')
            msg = msg.encode('utf-8')
            s.send(msg)
              
    except : 
        print('Error')
        s.close()
        return
        

t = Thread(target = clientSend)
t.start()  

import sys   

try:
    while True:
        recv_msg = s.recv(BUFF_SIZE)
        recv_msg = recv_msg.decode('utf-8')
        if msg != "{quite}" : 
             print( '\n' , recv_msg)
        # recv 'quite' to close 
        else:
            print("I left chat")
            break
except: 
    print()
