from pymongo import MongoClient
import time

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['MyDatabase']
collection = db['MyCollection']
#MyUser=[{"name":"ofer","id":123456789}]

#x=collection.insert_many(MyUser)

while 1 :
	time.sleep(3.0)
	for document in collection.find():
		print (document)

