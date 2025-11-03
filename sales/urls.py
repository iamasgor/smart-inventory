from django.urls import path

from sales import views

urlpatterns = [
    path('', views.index, name='index'),
]