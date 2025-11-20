from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
@login_required(login_url='login')
def home_view(request):
    return render(request, 'accounts/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account_home')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'accounts/login.html')
