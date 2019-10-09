from django.urls import path, include
from accounts.views import logout, login, registration, user_profile
from home.views import home

urlpatterns = [
    path('', home, name='home'),
    path('profile/', user_profile, name='profile'),
]