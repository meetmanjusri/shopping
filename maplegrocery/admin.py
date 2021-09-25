from django.contrib import admin
from .models import *


class UnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_date', 'updated_date']
    list_filter = ['name', 'description', 'created_date', 'updated_date']
    prepopulated_fields = {'description': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'updated_date']
    list_filter = ['name', 'created_date', 'updated_date']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'price', 'available', 'product_unit', 'product_category',
                    'created_date', 'updated_date']
    list_filter = ['name', 'description', 'image', 'price', 'available', 'product_unit', 'product_category',
                   'created_date', 'updated_date']


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ['payment_card', 'total_price', 'created_date', 'updated_date']
    list_filter = ['payment_card', 'total_price', 'created_date', 'updated_date']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_receipt', 'item_product', 'item_product_price', 'created_date', 'updated_date']
    list_filter = ['item_receipt', 'item_product', 'item_product_price', 'created_date', 'updated_date']


admin.site.register(Unit, UnitAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Item, ItemAdmin)
