from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('api/products/', views.get_products, name='get_products'),
    path('api/add-product/', views.add_product, name='add_product'),
    path('api/delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('api/create-order/', views.create_order, name='create_order'),
]