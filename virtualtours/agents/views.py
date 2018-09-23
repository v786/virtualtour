from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
  return render(request, 'agents/index.html')

def login_try(request):
  return render(request, 'agents/login.html')
  
def signin(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('/agents/')
    else:
        # Return an 'invalid login' error message.
        return redirect('/agents/login')