from django.urls import path, include
from products.views import category

urlpatterns = [
    path('company', category, name='products'),
]