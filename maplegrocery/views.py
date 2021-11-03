from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from cart.forms import CartAddProductForm
from .tasks import order_created
from cart.cart import Cart
from .models import *
from .forms import *

now = timezone.now()


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


def product_list(request, category_name=None):
    category = None
    categorys = Category.objects.all()
    products = Product.objects.filter(created_date__lte=timezone.now())
    cart_product_form = CartAddProductForm()
    if category_name:
        category = get_object_or_404(Category, name=category_name)
        products = products.filter(category=category)
    return render(request, 'maplegrocery/product_list.html',
                  {'category': category,
                   'categorys': categorys,
                   'products': products,
                   'cart_product_form': cart_product_form})


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


def order_list(request):
    order = Order.objects.filter(created_date__lte=timezone.now())
    return render(request, 'maplegrocery/order_list.html',
                  {'orders': order})


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})


@login_required
def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        # update
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.updated_date = timezone.now()
            order.save()
            return redirect('maplegrocery:order_list')
    else:
        # edit
        form = OrderForm(instance=order)
    return render(request, 'maplegrocery/order_edit.html', {'form': form})


@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('maplegrocery:order_list')
