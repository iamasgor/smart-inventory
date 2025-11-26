from django import forms
from django.db import models

from .models import Unit, Product, User


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ["unit_name", "unit_short_name"]

class ProductForm(forms.ModelForm):
    product_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "productNameField", "placeholder": "Product Name"}),
    )

    product_code = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Product Code"})
    )

    product_description = forms.CharField(
        max_length=1000,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Product Description"})
    )

    product_price = forms.DecimalField(
        decimal_places=2,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Product Price"})
    )

    product_quantity = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Product Quantity"})
    )

    product_unit = forms.ModelChoiceField(
        queryset=Unit.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Unit",
    )

    product_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Product
        fields = ["product_name", "product_code", "product_description", "product_unit", "product_quantity", "product_price", "product_image"]