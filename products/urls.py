from django.urls import path, include
from products.views import products

urlpatterns = [
    path('products', products, name='products'),
]