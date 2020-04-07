from pymongo import MongoClient
import time

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['MyDatabase']
collection = db['MyCollection']

x = collection.delete_many({})
print(x.deleted_count, " documents deleted.")

for document in collection.find():
    print (document)
