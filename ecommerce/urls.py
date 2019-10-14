from django.contrib import admin
from django.urls import path, include
from accounts import urls as urls_accounts
from home import urls as urls_home
from products import urls as urls_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls_home)),
    path('accounts/', include(urls_accounts)),
    path('products/', include(urls_products)),
]
