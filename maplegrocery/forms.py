from django import forms
from .models import Unit, Product, Category, Order, OrderItem
from django.forms.widgets import DateInput


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ('name', 'description')


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
        fields = ('first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'preferred_date', 'preferred_time')
        # Reference: https: // stackoverflow.com / questions / 3367091 / whats - the - cleanest - simplest - to - get - running - datepicker - in -django
        # https: // stackoverflow.com / questions / 55404397 / how - to - use - timeinput - widget - in -django - forms
        widgets = {'preferred_date': DateInput(attrs={'type': 'date'}),
                   'preferred_time': forms.TimeInput(attrs={'type': 'time'})}


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('order', 'product', 'price', 'quantity', 'created_date')


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
