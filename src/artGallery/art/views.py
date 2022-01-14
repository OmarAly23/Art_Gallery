from pymongo import MongoClient
import collections as c
import json
from bson.json_util import dumps, loads
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
# import sys
# sys.path.append('..')
# sys.path.append('.')


connectToMongo = "mongodb+srv://Zach-den:artGallery%40cs470@cluster0.briba.mongodb.net/artGallery?retryWrites=true&w=majority"
client = MongoClient(connectToMongo)
dbname = client['artGallery']
collection_name = dbname['User']


# Create your views here.

def index(request):
    # you first want to make sure if there is an active session or not
    if 'user' in request.session:
        # user is logged in
        # and session is live
        current_user = request.session['user']
        name = current_user.split('@')
        collection_name_art = dbname['art']
        result = collection_name_art.find({})
        param = {
            'name': name[0],
            'records': result,
        }
        return render(request, '../templates/index.html', param)

    if request.method == 'POST':
        nameC = request.POST['yname']
        emailC = request.POST['email']
        msgC = request.POST['message']
        contact_to_be_added = {
            "fname": nameC,
            "email": emailC,
            "msg": msgC,
        }
        collection_nameC = dbname['contact']
        collection_nameC.insert_one(contact_to_be_added)

    collection_name_art = dbname['art']
    # result is a cursor pointing to all records in art table
    # we only want records from 1 to 5
    # skipping 0 and 4
    result = collection_name_art.find({})
    data = {
        'records': result,
    }
    return render(request, '../templates/index.html', data)


# A testing function
# should try and send all art records to the homepage for display
def send_art(request):
    collection_name2 = dbname['art']
    result = collection_name2.find({})
    # result should contain all the art in the art table, to send and display in index.html aka the homepage
    list_result = list(result)
    print(f'{list_result[2]["art_title"]}')
    for l in list_result:
        print(f'l of art title is {l["art_title"]}')

    return HttpResponse(list_result)

# should take in the values
def sign_in(request):
    if request.method == 'POST':
        print('HI')
        # check if user is already registered
        # else send him to the sign up page
        # need to make sure that same user cannot register twice
        email = request.POST['email']
        password = request.POST['password']
        user_record = {
            "email_id": email,
            "password": password
        }
        for key, value in request.session.items():
            print(f'printing key and value of session {key} => {value}')
        retval = collection_name.find({"email_id": email}).count()
        # retval returning 0 indicates that the user is not registered
        if retval == 0:
            print(f'retval {retval}')
            return render(request, '../templates/error.html')
        else:
            print(f'retval {retval}')
            validate_pass = collection_name.find(user_record).count()
            if validate_pass == 1:
                request.session['user'] = email
                collection_name_user = dbname['User']
                userRecord = collection_name_user.find_one({"email_id": email})
                fname = userRecord['first_name']
                collection_name_art = dbname['art']
                result = collection_name_art.find({})
                param = {
                    'email': email,
                    'name': fname,
                    'records': result,
                }
                print(f'the current user logged in: {request.session["user"]}')
                return render(request, '../templates/index.html', param)
            else:
                return render(request, '../templates/error.html')

    return render(request, '../templates/logIn.html')


def log_out(request):
    try:
        del request.session['user']
        logout(request)
    except:
        return redirect('sign_in')
    return redirect('sign_in')


def sign_up(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        em = request.POST['email']
        passw = request.POST['password']
        user_to_be_added = {
            "email_id": em,
            "password": passw,
            "first_name": fname,
            "last_name": lname
        }
        # you cannot use the same email twice
        # check if the email is already registered
        # this part should check if an email already exists
        # retval should be 1 when the record exists and zero when it does not exist
        retval = collection_name.find({"email_id": em}).count()
        if retval == 0:
            print(f'Before we insert value, print retval: {retval}')
            collection_name.insert_one(user_to_be_added)
            return render(request, '../templates/logIn.html')
        else:
            print(f'Error side, print retval: {retval}')
            return render(request, '../templates/error.html')
        print('User has been added!')
    return render(request, '../templates/signUp.html')



def artist(request, name):
    artistName = {
        'name': name
    }
    return render(request, '../templates/artist.html', artistName)


# create a bookmark page for user
def bookmark(request):
    return render(request, '../templates/bookmark.html')