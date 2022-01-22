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
        # check if an user is an admin too or not
        try:
            result = collection_name_admin = dbname['admin']
            if result is not None:
                flag = 1
            else:
                flag = 0
        except:
            return render(request, './error.html')
        # user is logged in
        # and session is live
        current_user = request.session['user']
        name = current_user.split('@')
        collection_name_art = dbname['art']
        result = collection_name_art.find({})
        param = {
            'name': name[0],
            'records': result,
            'flag': flag
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
    collection_name_art = dbname["Artist"]
    retval = collection_name_art.find_one({"name": name})
    fname = retval['name']
    predob = str(retval['DOB'])
    country = retval['country']
    dob = predob.split(' ')
    pic = retval['pic']
    wiki = retval['wikiLink']
    try:
        dict = []
        listOfRecords = []
        collection_name_art = dbname['art']
        count = 0
        lRecords = list(retval['art'])

        # extract the IDs
        for l in lRecords:
            if isinstance(l, list):
                for records in l:
                    # print(f'Records are {records}')
                    listOfRecords.append(records)
            else:
                listOfRecords.append(l)

        # print(listOfRecords)

        # print(lRecords)
        for record in listOfRecords:
            # print(f'printing record {record}')
            count += 1
            retval = collection_name_art.find_one({"_id": record})
            # print(f'retval is {retval}')
            dict.append(retval)
    except:
        return render(request, './error.html')

    artistRec = {
        'firstName': fname,
        'DOB': dob[0],
        'art': dict,
        'country': country,
        'counter': count,
        'pic' : pic,
        'wiki': wiki
    }

    for items in retval:
        print(items)

    return render(request, '../templates/artist.html', artistRec)


# create a bookmark page for user
def bookmark(request):
    if 'user' in request.session:
        current_user = request.session['user']
        # print(current_user)
        collection_name_userArt = dbname['User']
        userRecord = collection_name_userArt.find_one({"email_id": current_user})
        fname = userRecord['first_name']

        try:
            dict = []
            listOfRecords = []
            collection_name_art = dbname['art']
            count = 0
            lRecords = list(userRecord['favourite'])

            # extract the IDs
            for l in lRecords:
                if isinstance(l, list):
                    for records in l:
                        # print(f'Records are {records}')
                        listOfRecords.append(records)
                else:
                    listOfRecords.append(l)

            # print(listOfRecords)

            # print(lRecords)
            for record in listOfRecords:
                # print(f'printing record {record}')
                count += 1
                retval = collection_name_art.find_one({"_id": record})
                # print(f'retval is {retval}')
                dict.append(retval)
        except:
            return render(request, './error.html')

        param = {
            'firstName': fname,
            'favourite': dict,
            'counter': count
        }

        return render(request, '../templates/bookmark.html', param)

    return render(request, '../templates/error.html')


def addToFav(request, button_id):
    if 'user' in request.session:
        if request.method == 'POST':
            # print('About to print something')
            # print(button_id)
            # print(list(request.POST.items()))
            email = request.session['user']
            collection_name_user = dbname['User']
            userRecord = collection_name_user.find_one({"email_id": email})
            # print(list(userRecord))
            # print(userRecord['favourite'])
            listToCheck = list(userRecord['favourite'])
            listOfRecords = []

            # extract the IDs
            for l in listToCheck:
                if isinstance(l, list):
                    for records in l:
                        # print(f'Records are {records}')
                        listOfRecords.append(records)
                else:
                    listOfRecords.append(l)

            #
            # print('Printing the list to check')
            # print(listOfRecords)
            fname = userRecord['first_name']
            collection_name_art = dbname['art']
            result = collection_name_art.find({})
            param = {
                'email': email,
                'name': fname,
                'records': result,
            }
            # insert into User's favourites
            res = collection_name_art.find_one({'artist_id': button_id})
            # print(list(res))
            # print(res['_id'])
            art_id = res['_id']
            try:

                # userInfo = collection_name_user.find({"email_id": email}, {'favourite': [art_id]}).count()
                # print('I should now print the list to check')
                user_info = 0
                for uRec in listOfRecords:
                    if uRec == art_id:
                        print(f'The current record is {uRec} and the art id is {art_id}')
                        user_info = 1

                print(f'User info is {user_info}')
                if user_info > 0:
                    # user has already favourited this art
                    # print('This record already exists')
                    return render(request, './error.html')
                else:
                    # continue
                    # print('This record does not exist')
                    collection_name_user.update_one(
                        {'email_id': email},
                        {'$push':
                             {'favourite': [art_id]}
                         }
                    )
                    # print('Inserted into user')
                    # return render(request, './addedToFav.html')
            except:
                print('error inserting')
                return render(request, './error.html')

            return render(request, './success.html')
    return render(request, './logIn.html')


def removeFav(request, button_id):
    if 'user' in request.session:
        if request.method == 'POST':
            try:
                print('Just entered here')
                collection_name_user = dbname['User']
                user_email = request.session['user']
                userRecord = collection_name_user.find_one({"email_id": user_email})

                listToCheck = list(userRecord['favourite'])
                print(listToCheck)

                collection_name_art = dbname['art']
                # result = collection_name_art.find({})
                res = collection_name_art.find_one({'artist_id': button_id})
                art_id = res['_id']
                print(f'art id is {art_id}')

                try:
                    collection_name_user.update_one(
                        {'email_id': user_email},
                        {'$pull':
                             {'favourite': [art_id]}
                         }
                    )
                    print('Delete Succeeded')
                except:
                    print('Error deleting')
                    return render(request, './error.html')

            except:
                print('Could not pull')
                return render(request, './error.html')

            return render(request, './removedFromFav.html')
    print('Here')
    return render(request, './error.html')


def admin(request):
    if 'user' in request.session:
        try:
            collection_name_admin = dbname['admin']
            # get user collection
            collection_name_user = dbname['User']
            result = collection_name_admin.find({})
            tmp = collection_name_admin.find({})
            tmp = list(tmp)
            # print('print tmp list')
            # print(tmp)
            # print(tmp[0]['user_id'])
            userID = tmp[0]['user_id']

            # get corresponding user data
            userResult = collection_name_user.find({'_id': userID})
            # userResult = list(userResult)
            # print('Attempting to print user result')
            # print(userResult)
            if result is not None:
                print('You are an admin')

            if request.method == 'POST':
                collection_name_art = dbname['art']
                art_count = collection_name_art.find({}).count()
                artistID = 'R' + str(art_count + 3)
                print(artistID)
                artTitle = request.POST['artTitle']
                artist = request.POST['artist']
                art = request.POST['art']
                cat = request.POST['artCat']
                year_C = request.POST['yearCreated']
                artD = request.POST['artDesc']
                new_art = {
                    "artist_id": artistID,
                    "art_title": artTitle,
                    "artist": artist,
                    "art_description": artD,
                    "s3": art,
                    "art_category": cat,
                    "year_created": year_C

                }
                print("new art has been created")
                retval = collection_name_art.find({"art_title": artTitle}).count()
                if retval == 0:
                    print(f'Before we insert value, print retval: {retval}')
                    collection_name_art.insert_one(new_art)
                    print("new art has been added")
        except:
            print('could not compute anything')
            return render(request, './error.html')
        print(result)
        param = {
            'userRec': userResult,
            'adminRecords': result,
        }
        return render(request, './admin.html', param)

    return render(request, './error.html')
