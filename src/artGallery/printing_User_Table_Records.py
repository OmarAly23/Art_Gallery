from db_connect import dbname

collection_name = dbname["User"]

count = collection_name.count()
print(count)

result = collection_name.find({})

for element in result:
    print(element)