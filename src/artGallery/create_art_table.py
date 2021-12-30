from db_connect import dbname

collection_name = dbname['art']

art1 = {
    "artist_id": "R1",
    "art_title": "",
    "art_document": "",
    "artist": "Nero n sei",
}

art2 = {
    "artist_id": "R2",
    "art_title": "",
    "art_document": "",
    "artist": "Gabr Jurk",
}

collection_name.insert_many([art1, art2])

count = collection_name.count()
print(count)

result = collection_name.find({})

for element in result:
    print(element)

