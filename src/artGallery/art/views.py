from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

# from ..db_connect import dbname
# collection_name = dbname['User']

# Create your views here.

def index(request):
    return render(request, '../templates/index2.html')

# should take in the values
def sign_in(request):

    return render(request, '../templates/sign_in.html')

def sign_up(request):
    return render(request, '../templates/sign_up.html')
# Create a function for handling users


# Create a function for handling Art


# # Create a function for the sign in/up
# def signup_view(request):
