from django.urls import path

from products import views

urlpatterns = [
    path('unit/', views.unit_list, name='unit_list'),
    path("unit/<int:pk>/", views.unit_detail, name="unit_detail"),
    path("unit/create/", views.create_unit, name="create_unit"),

    path("product/", views.product_list , name="product_list"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("product/search", views.search_product, name="search_product"),
    path("product/create/", views.create_product, name="create_product"),
    path("product/<int:pk>/edit/", views.update_product, name="update_product"),
]