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


@login_required
def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_date = timezone.now()
            product.save()
            return redirect('maplegrocery:product_list')
    else:
        form = ProductForm()
        # print("Else")
    return render(request, 'maplegrocery/product_new.html', {'form': form})


@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        # update
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.updated_date = timezone.now()
            product.save()
            return redirect('maplegrocery:product_list')
    else:
        # edit
        form = ProductForm(instance=product)
    return render(request, 'maplegrocery/product_edit.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('maplegrocery:product_list')


def category_list(request):
    category = Category.objects.filter(created_date__lte=timezone.now())
    return render(request, 'maplegrocery/category_list.html',
                  {'categorys': category})


@login_required
def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_date = timezone.now()
            category.save()
            return redirect('maplegrocery:category_list')
    else:
        form = CategoryForm()
    return render(request, 'maplegrocery/category_new.html', {'form': form})


@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        # update
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.updated_date = timezone.now()
            category.save()
            return redirect('maplegrocery:category_list')
    else:
        # edit
        form = CategoryForm(instance=category)
    return render(request, 'maplegrocery/category_edit.html', {'form': form})


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('maplegrocery:category_list')