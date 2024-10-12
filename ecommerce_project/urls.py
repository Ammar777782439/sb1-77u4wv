from django.contrib import admin
from django.urls import path
from store import views as store_views
from reports import views as report_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', store_views.product_list, name='product_list'),
    path('product/<int:pk>/', store_views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', store_views.add_to_cart, name='add_to_cart'),
    path('cart/', store_views.cart, name='cart'),
    path('checkout/', store_views.checkout, name='checkout'),
    path('order-confirmation/', store_views.order_confirmation, name='order_confirmation'),
    path('reports/sales/', report_views.generate_sales_report, name='sales_report'),
    path('reports/inventory/', report_views.generate_inventory_report, name='inventory_report'),
]