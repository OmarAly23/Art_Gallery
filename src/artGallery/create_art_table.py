from db_connect import dbname
collection_name = dbname['art']

art_1 = {
    "art_id": "RR00012343",
    "image": "",
    "art_title": "Berzerk",
    "art_type": "Manga",
}


collection_name.insert_one(art_1)

