from django.urls import path

from sales import views

urlpatterns = [
    path('', views.home_view, name='sales_home'),
    path('core/', views.core_view, name='core'),
]