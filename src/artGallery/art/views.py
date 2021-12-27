from pymongo import MongoClient

from django.shortcuts import render
from django.http import HttpResponse

# import sys
# sys.path.append('..')
# sys.path.append('.')


connectToMongo = "mongodb+srv://Zach-den:artGallery%40cs470@cluster0.briba.mongodb.net/artGallery?retryWrites=true&w=majority"
client = MongoClient(connectToMongo)
dbname = client['artGallery']
collection_name = dbname['User']


# Create your views here.

def index(request):
    return render(request, '../templates/index2.html')


# should take in the values
def sign_in(request):
    return render(request, '../templates/sign_in.html')


def sign_up(request):
    if request.method == 'POST':
        em = request.POST['email']
        passw = request.POST['password']
        user_to_be_added = {
            'email': em,
            'password': passw
        }
        collection_name.insert_one(user_to_be_added)
        print('User has been added!')
    return render(request, '../templates/sign_up.html')
# Create a function for handling users


# Create a function for handling Art


# # Create a function for the sign in/up
# def signup_view(request):
