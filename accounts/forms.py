from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from .models import UserRegistrationModel

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput)

    class Meta:
        model = UserRegistrationModel
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'street_address_1',
            'street_address_2',
            'county',
            'town_or_City',
            'postcode',
            'phone_number',
        ]


class RegisterUserChangeForm(UserChangeForm):
    class Meta:
        model = UserRegistrationModel
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'street_address_1',
            'street_address_2',
            'county',
            'town_or_City',
            'postcode',
            'phone_number',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'You must use a unique email address')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError('Password input unsuccessfull')

        if password1 != password2:
            raise ValidationError('Password does not match')
        return password2
