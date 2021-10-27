from django.contrib import admin
from .models import Unit, Category, Product, Order, OrderItem


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


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'payment_card',
                    'created_date', 'updated_date', 'paid']
    list_filter = ['paid', 'created_date', 'updated_date']
    inlines = [OrderItemInline]


admin.site.register(Unit, UnitAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
