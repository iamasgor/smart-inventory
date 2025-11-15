from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.login_view, name='signup'),
]