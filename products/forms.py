from django import forms
from .models import Unit, Product


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ["unit_name", "unit_short_name"]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "product_code", "product_description", "product_unit", "product_quantity", "product_price", "product_image"]