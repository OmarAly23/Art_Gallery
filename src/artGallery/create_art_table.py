from db_connect import dbname
# libraries to help with image storage
from PIL import Image
import io
from bson.binary import Binary
import matplotlib.pyplot as plt

collection_name = dbname['art']


# im = Image.open('./art/static/admin/img/VirginOfTheRocks.jpg')
# image_bytes = io.BytesIO()
# im.save(image_bytes, format='JPEG')
# # image variable contains the actual byte representation of the image
# image = image_bytes.getvalue()
#
# im1 = Image.open('./art/static/admin/img/Liberty.jpg')
# image_bytes1 = io.BytesIO()
# im1.save(image_bytes1, format="JPEG")
# image1 = image_bytes1.getvalue()
#
#
# im2 = Image.open('./art/static/admin/img/thePresistenceOfMemory.jpg')
# image_bytes2 = io.BytesIO()
# im2.save(image_bytes2, format='JPEG')
# # image variable contains the actual byte representation of the image
# image2 = image_bytes2.getvalue()
#
# im3 = Image.open('./art/static/admin/img/wanderer.jpg')
# image_bytes3 = io.BytesIO()
# im3.save(image_bytes3, format="JPEG")
# image3 = image_bytes3.getvalue()
#
# # art1 = {
# #     "artist_id": "R3",
# #     "art_title": "Six Tusan Poets",
# #     "art_document": image,
# #     "artist": "Giorgio Vasari",
# #     "art_description": "depicting a group of Italian Humanists (Dante Alighieri, Giovanni Boccaccio, Petrarch, Cino da Pistoia, Guittone dArezzo, and Guido Cavalcanti)",
# # }
# #
# # art2 = {
# #     "artist_id": "R4",
# #     "art_title": "Son of Man",
# #     "art_document": image1,
# #     "artist": "Rene Magritte",
# #     "art_description": "At least it hides the face partly well, so you have the apparent face, the apple, hiding the visible but hidden, the face of the person. It&apos;s something that happens constantly. Everything we see hides another thing, we always want to see what is hidden by what we see. There is an interest in that which is hidden and which the visible does not show us. This interest can take the form of a quite intense feeling, a sort of conflict, one might say, between the visible that is hidden and the visible that is present.",
# # }
# #
# # art3 = {
# #     "artist_id": "R5",
# #     "art_title": "Virgin of the Rocks (1503-1506)",
# #     "art_document": image,
# #     "artist": "Leonardo da Vinci",
# #     "art_description": "When we look at Virgin of the Rocks, the subject matter of this painting is the Virgin Mother Mary with two infants: one is Jesus Christ, and the other is John the Baptist. They are accompanied by the archangel Gabriel to the right-hand side. The environment around the figures is quite mysterious in nature, depicting various rocky, almost cave-like structures in the background with a pool of water and some foliage with rocks in the foreground.",
# # }
# #
# # art4 = {
# #     "artist_id": "R6",
# #     "art_title": "The Presistence of Memory (1931)",
# #     "art_document": image1,
# #     "artist": "Salvador Dali",
# #     "art_description": "Those limp watches are as soft as overripe cheese—indeed, they picture “the camembert of time,” in Dalí&apos;s phrase. Here time must lose all meaning. Permanence goes with it: ants, a common theme in Dalí&apos;s work, represent decay, particularly when they attack a gold watch, and they seem grotesquely organic. The monstrous fleshy creature draped across the painting&apos;s center is at once alien and familiar: an approximation of Dalí&apos;s own face in profile, its long eyelashes seem disturbingly insect-like or even sexual, as does what may or may not be a tongue oozing from its nose like a fat snail.",
# # }
#
# art5 = {
#     "artist_id": "R7",
#     "art_title": "Liberty Leading the People (1830)",
#     "art_document": image2,
#     "artist": "Eugene Delacroix",
#     "art_description": "Liberty Leading the People (1830) by Eugène Delacroix, depicting the theater of war during the French July Revolution (July 28, 1830)",
# }
#
# art6 = {
#     "artist_id": "R8",
#     "art_title": "Wanderer Above the Sea of Fog (1818)",
#     "art_document": image3,
#     "artist": "Rene Magritte",
#     "art_description": "The painting was done during a time in which exploration was largely romanticized by much of Europe and the United States. Friedrich&apos;s work appears to convey the sense of wonder and adventure that was so often sought after among the many explorers of the early 19th century."
# }
#
#
# #
# #
# collection_name.insert_many([art5, art6])

count = collection_name.count()
print(count)

result = collection_name.find({})

for element in result:
    plt_img = Image.open(io.BytesIO(element['art_document']))
    plt.imshow(plt_img)
    plt.show()

