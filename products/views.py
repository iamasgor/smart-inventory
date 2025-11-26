from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Unit, Product
from .forms import UnitForm, ProductForm


def unit_list(request):
    units = Unit.objects.all().order_by("-created_at")
    return render(request, "products/unit/unit_list.html", {"units": units})

def unit_detail(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    return render(request, "products/unit/unit_view.html", {"unit": unit})

@login_required
def create_unit(request):
    if request.method == "POST":
        form = UnitForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            return redirect("unit_detail", pk=post.pk)
    else:
        form = UnitForm()
    return render(request, "products/unit/unit_form.html", {"form": form})

def product_list(request):
    products = Product.objects.all().order_by("-created_at")
    return render(request, "products/product/product_list.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product/product_view.html", {"product": product})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product/product_delete.html", {"product": product})

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            return redirect("product_detail", pk=post.pk)
    else:
        form = ProductForm()
    return render(request, "products/product/product_form.html", {"form": form})

def search_product(request):
    pass
