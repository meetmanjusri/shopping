from django import forms
from .models import Unit, Product, Category


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ('name', 'description')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description','image','price','available', 'product_unit','product_category')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)