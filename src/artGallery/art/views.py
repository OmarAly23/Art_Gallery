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
    if request.method == 'POST':
        # check if user is already registered
        # else send him to the sign up page
        email = request.POST['email']
        password = request.POST['password']
        user_record = {
            "email": email,
            "password": password
        }
        retval = collection_name.find(user_record)
        if retval is None:
            return render(request, '../templates/success.html')
        else:
            return render(request, '../templates/error.html')
    return render(request, '../templates/sign_in.html')


def sign_up(request):
    if request.method == 'POST':
        em = request.POST['email']
        passw = request.POST['password']
        user_to_be_added = {
            "email": em,
            "password": passw
        }
        retval = collection_name.find(user_to_be_added)
        if retval is None:
            return render(request, '../templates/error.html')
        else:
            return render(request, '../templates/success.html')
        print('User has been added!')
    return render(request, '../templates/sign_up.html')


