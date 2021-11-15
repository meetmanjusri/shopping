from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail

from .cart import Cart
from .models import *
from .forms import *
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

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


def product_list(request):
    products = []
    if request.method == "GET":
        query = request.GET.get('search')
        print(query)
        if query == '' or query is None:
            query = 'None'
            products = Product.objects.filter(created_date__lte=timezone.now())
        else:
            products = Product.objects.filter(name__icontains=query)
    cart_product_form = CartAddProductForm()
    return render(request, 'maplegrocery/product_list.html',
                  {'products': products,
                   'cart_product_form': cart_product_form,
                   'query': query})

@login_required
def product_detail(request):
    product = Product.objects.filter(created_date__lte=timezone.now())
    return render(request, 'maplegrocery/product_detail.html',
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
            return redirect('maplegrocery:product_detail')
    else:
        # edit
        form = ProductForm(instance=product)
    return render(request, 'maplegrocery/product_edit.html', {'form': form})


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('maplegrocery:product_detail')


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


def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_MAPLE,
                          [order.email])
    return mail_sent


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
            order_created(order.id)
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


@staff_member_required
# @login_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(settings.STATIC_FILES + '/css/pdf.css')])
    return response


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
    cart.add(product=product,
         quantity=cd['quantity'],
         override_quantity=cd['override'])
    return redirect('maplegrocery:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('maplegrocery:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})