from django.shortcuts import render, reverse, redirect
from django.conf import settings
from .forms import Signinform, Signupform
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate
from .models import Signin,Signup



from .mixins import (

	RedirectParams,
	APIMixin
)

'''
Basic view for selecting query
'''
def index(request):

	if request.method == "POST":
		cat = request.POST.get("cat", None)
		if cat:
			return RedirectParams(url = 'main:results', params = {"cat": cat})

	return render(request, 'main/index.html', {})



'''
Basic view for displaying results
'''
def results(request):

	cat = request.GET.get("cat", None)

	if cat:
		results = APIMixin(cat=cat).get_data()
		print (results)

		if results:
			context = {
				"results": results,
				"cat": cat,
			}

			return render(request, 'main/results.html', context)
	
	return redirect(reverse('main:home'))


def signup(request):
    if request.method=='POST':
        fm=Signupform(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email  =fm.cleaned_data['email']
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
        user=User.objects.create_user(email=email,username=username,password=password)
        user.first_name=name
        user.save()
        messages.success(request,'user created successfully')
        return redirect(reverse('main:home'))

    fm=Signupform()
    d={'fm':fm}
    return render(request,'signup.html',d)


def signin(request):
    if request.method=='POST':
        fm=Signinform(request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
        user=authenticate(username=username,password=password)      
        if user is not None:
            auth_login(request,user)
            return redirect(reverse('main:home'))
        else:
            messages.error(request,'invalid username or password')
            return render(request,'invalid.html')

    fm=Signinform()
    d={'fm':fm}
    return render(request,'signin.html',d)


def logout(request):
    auth_logout(request)
    return redirect(reverse('main:home'))



def action(request):
    return render(request,'action.html')

def invalid(request):
	return render(request,'invalid.html')