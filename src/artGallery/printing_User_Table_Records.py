import pymongo
from django.conf import settings
from pymongo import MongoClient

connectToMongo = "mongodb+srv://Zach-den:artGallery%40cs470@cluster0.briba.mongodb.net/artGallery?retryWrites=true&w=majority"
client = MongoClient(connectToMongo)
dbname = client['artGallery']
collection_name = dbname["User"]

count = collection_name.count()
print(count)

result = collection_name.find({})

for element in result:
    print(element)