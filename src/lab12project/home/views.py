from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, '../templates/index.html')


def index2(request):
    return render(request, '../templates/index2.html')


# Create a function for handling users

# Create a function for handling Art