from db_connect import dbname

collection_name = dbname['art']

artist_1 = {
    "artist_id": "R1",
    "name": "Nero n sei",
    "DOB": "7-4-1994",
    "wiki_page": " ",
    "country": "Japan",
    "state": "tokyo"
}

artist_2 = {
    "artist_id": "R2",
    "name": "Gabr Jurk",
    "DOB": "9-4-1991",
    "wiki_page": " ",
    "country": "UK",
    "state": "London"
}

collection_name.insert_many([artist_1, artist_2])

count = collection_name.count()
print(count)

result = collection_name.find({})

for element in result:
    print(element)

