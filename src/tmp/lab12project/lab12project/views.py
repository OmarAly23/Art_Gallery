from django.shortcuts import render
from .models import MyUserTable
from .forms import MyForm
from datetime import datetime

from django.template import loader
from django.http import HttpResponse

from django.conf import settings


def home(request):
	return render(request, './templates/home.html')



def entry(request):
	form = MyForm()
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():
			foo = MyUserTable(
				name=form.cleaned_data['name'],
				role=form.cleaned_data['role'],
				email=form.cleaned_data['email'],
				created_on=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
			)
			foo.save()
		else:
			return render(request,  './templates/entry.html', {'form': form, 'error': 'Bad data entry.'})
		return render(request, './templates/entry.html', {'form': MyForm()})
	return render(request, './templates/entry.html', {'form': form})


def search(request):
	template = loader.get_template('./templates/search.html')

	#get the emil from url parameters
	foo = request.GET.get('email')

	#get the record from the table using hash key
	if foo != None and foo != '':
		user = MyUserTable.get(email=foo)

		#prepare object to be send to the template
		context = {
			'user33' : user
		}

	return HttpResponse(template.render(context, request))

def delete(request):
	template = loader.get_template('./templates/delete.html')

	foo = request.GET.get('email')

	if foo != None and foo != '':
		user = MyUserTable.get(email=foo)

		#Save record information before deletetion
		user_temp = {}
		user_temp['email']=user.email
		user_temp['name']=user.name
		user_temp['role']=user.role
		user_temp['created_on']=user.created_on

		#delete
		user.delete()

		#prepare object to be send to the template
		context = {
			'user' : user_temp
		}

	return HttpResponse(template.render(context, request))
