from pymongo import MongoClient

from django.shortcuts import render, redirect
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
    return render(request, '../templates/index.html')


# should take in the values
def sign_in(request):
    if request.method == 'POST':
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
                name = email.split('@')
                userInfo = {
                    'email': email,
                    'name': name[0]
                }
                print(f'the current user logged in: {request.session["user"]}')
                return render(request, '../templates/logIn.html', userInfo)
            else:
                return render(request, '../templates/error.html')

    return render(request, '../templates/logIn.html')


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')


def sign_up(request):
    if request.method == 'POST':
        em = request.POST['email']
        passw = request.POST['password']
        user_to_be_added = {
            "email_id": em,
            "password": passw
        }
        # you cannot use the same email twice
        # check if the email is already registered
        # this part should check if an email already exists
        # retval should be 1 when the record exists and zero when it does not exist
        retval = collection_name.find({"email_id": em}).count()
        if retval == 0:
            print(f'Before we insert value, print retval: {retval}')
            collection_name.insert_one(user_to_be_added)
            return render(request, '../templates/success.html')
        else:
            print(f'Before we insert value, print retval: {retval}')
            return render(request, '../templates/error.html')
        print('User has been added!')
    return render(request, '../templates/sign_up.html')




# Creating and testing cookie sessions

# def cookie_session(request):
#     request.session.set_test_cookie()
#     return HttpResponse("<h1>Dataflair</h1>")
#
# def cookie_delete(request):
#     if request.session.test_cookie_worked():
#         request.session.delete_test_cookie()
#         response = HttpResponse("dataflair</br>")
#     else:
#         response = HttpResponse("cookie was not accepted<br>")
#     return response
#
#
# def create_session(request):
#     request.session['email'] = 'email'
#     request.session['password'] = 'password'
#     return HttpResponse('<h1>The session started for email and password</h1>')
#     # access_session(request, email, password)

# def access_session(request, email, password):
#     response = "<h1>User just logged in</h1><br>"
#     if request.session.get(email):
#         response += f"User email: {request.session.get(email)}"
#     if request.session.get(password):
#         response += f"User password: {request.session.get(password)}"
#         return HttpResponse(response)
#     else:
#         return redirect('/')
#





