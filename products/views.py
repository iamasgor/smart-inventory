from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Unit
from .forms import UnitForm

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
            post.author = request.user
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = UnitForm()
    return render(request, "products/unit/unit_form.html", {"form": form})