from django.urls import path, include
from products.views import products

urlpatterns = [
    path('company', products, name='products'),
]