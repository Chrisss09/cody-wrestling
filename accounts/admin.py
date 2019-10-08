from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import RegisterUserForm, RegisterUserChangeForm
from .models import UserRegistrationModel

class CustomUserRegisterAdmin(admin.ModelAdmin):
    add_form = RegisterUserForm
    form = RegisterUserChangeForm
    model = UserRegistrationModel

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff',)

    fields = (
        'email', 
        'username', 
        'first_name', 
        'last_name',
        'street_address_1',
        'street_address_2',
        'county',
        'town_or_City',
        'postcode',
        'phone_number',
        'is_staff',
        'last_login',
        'is_superuser',
        'is_active',
        'date_joined',
        'groups',
        'user_permissions', 
    )

admin.site.register(UserRegistrationModel, CustomUserRegisterAdmin)