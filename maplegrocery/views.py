from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import *
from .forms import *

now = timezone.now()


def home(request):
    products = Product.objects.filter(created_date__lte=timezone.now())
    category = Category.objects.filter(created_date__lte=timezone.now())
    return render(request, 'maplegrocery/home.html',
                  {'maplegrocery': home, 'products': products, 'categorys': category})


def unit_list(request):
    unit = Unit.objects.filter(created_date__lte=timezone.now())
    return render(request, 'maplegrocery/unit_list.html',
                  {'units': unit})


@login_required
def unit_new(request):
    if request.method == "POST":
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.created_date = timezone.now()
            unit.save()
            return redirect('maplegrocery:unit_list')
    else:
        form = UnitForm()
        # print("Else")
    return render(request, 'maplegrocery/unit_new.html', {'form': form})


@login_required
def unit_edit(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    if request.method == "POST":
        # update
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.updated_date = timezone.now()
            unit.save()
            return redirect('maplegrocery:unit_list')
    else:
        # edit
        form = UnitForm(instance=unit)
    return render(request, 'maplegrocery/unit_edit.html', {'form': form})


@login_required
def unit_delete(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    unit.delete()
    return redirect('maplegrocery:unit_list')


def product_list(request):
    product = Product.objects.filter(created_date__lte=timezone.now())
    return render(request, 'maplegrocery/product_list.html',
                  {'products': product})


def category_list(request):
    category = Category.objects.filter(created_date__lte=timezone.now())
    return render(request, 'maplegrocery/category_list.html',
                  {'categorys': category})
