from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def index_view(request):
    return render(request, 'accounts/index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'accounts/index.html')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'accounts/login.html')
