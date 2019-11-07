from django.urls import path, include
from products.views import category, view_products
# , view_more_info

urlpatterns = [
    path('company', category, name='products'),
    path('company/<category>/', view_products, name='view_products'),
    # path('company/<category>/<slug:slug_id>/', view_more_info, name='view_more_info'),
]