from django.contrib import admin
from django.urls import path
from accounts.views import login, logout, registration, user_profile
from home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('profile/', user_profile, name='profile'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', registration, name='registration'),
]
