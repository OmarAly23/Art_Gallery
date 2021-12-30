from db_connect import dbname
# libraries to help with image storage
from PIL import Image
import io
from bson.binary import Binary
import matplotlib.pyplot as plt

collection_name = dbname['art']


im = Image.open('./art/static/admin/img/Berserk_Manga.jpeg')
image_bytes = io.BytesIO()
im.save(image_bytes, format='JPEG')
# image variable contains the actual byte representation of the image
image = image_bytes.getvalue()

im1 = Image.open('./art/static/admin/img/Sequence.jpeg')
image_bytes1 = io.BytesIO()
im1.save(image_bytes1, format="JPEG")
image1 = image_bytes1.getvalue()

# art1 = {
#     "artist_id": "R1",
#     "art_title": "Berserk Manga",
#     "art_document": image,
#     "artist": "Nero n sei",
# }
#
# art2 = {
#     "artist_id": "R2",
#     "art_title": "Sequence",
#     "art_document": image1,
#     "artist": "Gabr Jurk",
# }
#
# collection_name.insert_many([art1, art2])

count = collection_name.count()
print(count)

result = collection_name.find({})

for element in result:
    plt_img = Image.open(io.BytesIO(element['art_document']))
    plt.imshow(plt_img)
    plt.show()

