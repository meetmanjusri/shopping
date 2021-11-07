from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'maplegrocery'

urlpatterns = [
        path('', views.product_list, name='product_list'),
        # re_path(r'^home/$', views.home, name='home'),
        path('unit_list', views.unit_list, name='unit_list'),
        path('unit/create/', views.unit_new, name='unit_new'),
        path('unit/<int:pk>/edit/', views.unit_edit, name='unit_edit'),
        path('unit/<int:pk>/delete/', views.unit_delete, name='unit_delete'),
        path('product_list', views.product_list, name='product_list'),
        path('product/create/', views.product_new, name='product_new'),
        path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
        path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
        path('category_list', views.category_list, name='category_list'),
        path('category/create/', views.category_new, name='category_new'),
        path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
        path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),
        path('order_list', views.order_list, name='order_list'),
        path('order/create/', views.order_create, name='order_create'),
        path('order/<int:pk>/edit/', views.order_edit, name='order_edit'),
        path('order/<int:pk>/delete/', views.order_delete, name='order_delete'),
        path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
