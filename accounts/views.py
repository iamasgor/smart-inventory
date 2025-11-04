from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')


def login(request):
    return render(request, 'accounts/index.html')