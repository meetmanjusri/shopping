from django import forms
from .models import Unit, Product, Category, Order, OrderItem


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ('name', 'description', 'created_date')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'available', 'product_unit', 'product_category')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'braintree_id', 'paid')


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('order','product','price','quantity','created_date')

