from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.template.loader import render_to_string
from .models import Unit, Product
from .forms import UnitForm, ProductForm


def unit_list(request):
    units = Unit.objects.all().order_by("id")
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
    context = {
        "products": products,
        "form": ProductForm(),
    }
    return render(request, "products/product/product_list.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product/product_view.html", {"product": product})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product/product_delete.html", {"product": product})

@login_required
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            # render a single table row partial to send back to the client
            row_html = render_to_string("products/product/product_row.html", {"product": product}, request=request)
            response = HttpResponse(row_html)
            # trigger event on client so JS can close modal
            response["HX-Trigger"] = "productAdded"
            return response
        else:
            # If form is invalid, return the form with errors
            # Use HX-Retarget to replace the modal body instead of the table
            form_html = render_to_string("products/product/product_form_fields.html", {"form": form}, request=request)
            response = HttpResponse(form_html)
            response["HX-Retarget"] = "#product-form-container"
            response["HX-Reswap"] = "innerHTML"
            return response
    else:
        form = ProductForm()
    return render(request, "products/product/product_form.html", {"form": form})

@login_required
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            updated_product = form.save()
            # render the updated table row partial to send back to the client
            row_html = render_to_string("products/product/product_row.html", {"product": updated_product}, request=request)
            response = HttpResponse(row_html)
            # trigger event on client so JS can close modal
            response["HX-Trigger"] = "productUpdated"
            return response
        else:
            # If form is invalid, return the form with errors
            form_html = render_to_string("products/product/product_edit_form_fields.html", {"form": form, "product": product}, request=request)
            response = HttpResponse(form_html)
            response["HX-Retarget"] = "#product-edit-form-container"
            response["HX-Reswap"] = "innerHTML"
            return response
    else:
        # GET request - return the form populated with product data
        form = ProductForm(instance=product)
        form_html = render_to_string("products/product/product_edit_form_fields.html", {"form": form, "product": product}, request=request)
        return HttpResponse(form_html)

def search_product(request):
    pass
