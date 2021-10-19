from django.shortcuts import render
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


def product_list(request):
    product = Product.objects.filter(created_date__lte=timezone.now())
    return render(request, 'maplegrocery/product_list.html',
                  {'products': product})


def category_list(request):
    category = Category.objects.filter(created_date__lte=timezone.now())
    return render(request, 'maplegrocery/category_list.html',
                  {'categorys': category})
