from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, BookEvent
from .models import Booking
# Create your views here.


def index(request):
    form = BookEvent()
    if request.method == "POST":
        form = BookEvent(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
        else:
            form = RegisterForm()
    bookings = Booking.objects.all()
    return render(request, 'agents/index.html', {'eventform': form, 'bookings': bookings})


def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            return render(request, 'agents/login.html')
        else:
            form = RegisterForm()
    return render(request, 'agents/register.html', {'form': form})


def login_try(request):
    return render(request, 'agents/login.html')


def signout(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/agents/login')


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
