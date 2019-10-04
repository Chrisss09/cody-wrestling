from django.contrib import admin
from django.urls import path
from accounts.views import login, logout
from home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
