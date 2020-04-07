from socket import * 
from threading import Thread
from pymongo import MongoClient
import time

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['MyDatabase']
collection = db['MyCollection']

x = collection.delete_many({})



clients  = {}



def accept_connections():
    while True:
        con , add = s.accept()

        NewUser=[{"id":add[1]}]
        x=collection.insert_many(NewUser)


        print('{} has entered chat'.format(add[1]))
        con.send("Welcome to Chat, plz enter name ".encode('utf-8'))
        Thread(target=handleClient ,args=[ con,add[1] ]).start() # start thread to handle client

        		          
	    

def handleClient(con,id):
    name = con.recv(1024)
    name = name.decode("utf-8")
    MyUser=[{"name":name,"id":id}]
    print(name , id)
    
    myquery = { "id": id }
    newvalues = { "$set": { "name": name } }
    collection.update_one(myquery, newvalues)

    msg =  "welcome " + name + " write {quite} to exit form chat" 
    con.send(msg.encode("utf-8"))
    clients[con] = con
    sendToAll("{} has entered chat".format(name) , "" , con1 = con ) 
    try:
        while 1:
            msg = con.recv(BUFF_SIZE)
            msg = msg.decode('utf-8')
            print(name , msg , sep = ":")
            if msg != "{quite}":
                sendToAll( msg  ,name  , con1 = con)
            else :
                con.send("{quite}".encode("utf-8"))

                del clients[con] # remove from set
                sendToAll(" {} has left chat".format(name), "" , con1 = None)

                host, port = con.getpeername()
                myquery = { "id": port }
                collection.delete_one(myquery)

                con.close()
            

                break
    except:
            sendToAll(" {} has left chat".format(name), "" , con1 = None)

def sendToAll(msg , src  , con1): # keep track of no-defaut must be last 
    src = src +"::"+ msg
    msg = src.encode("utf-8")
    for con in clients:
        if con != con1:
             con.send(msg)

try:
    s = socket(AF_INET , SOCK_STREAM)
    s.setsockopt(SOL_SOCKET , SO_REUSEADDR , 1)    
    HOST = '127.0.0.1'
    PORT = 7788
    s.bind((HOST , PORT))
    s.listen(5)
    BUFF_SIZE = 1024
    t = Thread(target = accept_connections() )
    t.start()
    t.join()
    s.close()
    
    print("exit")
except:
    print("bye")
    exit()    
