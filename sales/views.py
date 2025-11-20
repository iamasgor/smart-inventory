from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'sales/home.html')

def core_view(request):
    return render(request, 'core/base.html')