from django.urls import path, include
from .views import logout, login, registration, user_profile

urlpatterns = [
    path('accounts/registration/', registration, name='registration'),
    path('accounts/logout/', logout, name='logout'),
    path('accounts/login/', login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]