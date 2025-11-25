from django.urls import path

from products import views

urlpatterns = [
    path('unit/', views.unit_list, name='unit_list'),
    path("unit/<int:pk>/", views.unit_detail, name="unit_detail"),
    path("unit/create/", views.create_unit, name="create_unit"),
]