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
        # need to make sure that same user cannot register twice
        email = request.POST['email']
        password = request.POST['password']
        user_record = {
            "email": email,
            "password": password
        }
        # this part should check if an email already exists
        check_email = collection_name.find({"email": email}).count()
        if check_email > 1:
            # hence, the email is already registered
            return HttpResponse('The email already exists!')
        retval = collection_name.find(user_record).count()
        if retval == 1:
            return render(request, '../templates/error.html')
        else:
            return render(request, '../templates/success.html')
    return render(request, '../templates/sign_in.html')


def sign_up(request):
    if request.method == 'POST':
        em = request.POST['email']
        passw = request.POST['password']
        user_to_be_added = {
            "email": em,
            "password": passw
        }
        # you cannot use the same email twice
        # check if the email is already registered
        retval = collection_name.find(user_to_be_added).count()
        if retval == 0:
            print(f'Before we insert value, print retval: {retval}')
            collection_name.insert_one(user_to_be_added)
            return render(request, '../templates/success.html')
        else:
            return render(request, '../templates/error.html')
        print('User has been added!')
    return render(request, '../templates/sign_up.html')


