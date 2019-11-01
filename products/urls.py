from django.urls import path, include
from products.views import category, view_products, view_more_info

urlpatterns = [
    path('company', category, name='products'),
    path('company/dvds/', view_products, name='view_products'),
    path('<dvd_id>/', view_more_info, name='view_more_info'),
]