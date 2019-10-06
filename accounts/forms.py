from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    street_address1 = forms.CharField(label="Address Line 1", max_length=40, required=False)
    street_address2 = forms.CharField(label="Address Line 2", max_length=40, required=False)
    county = forms.CharField(max_length=40, required=False)
    town_or_city = forms.CharField(max_length=40, required=False)
    postcode = forms.CharField(max_length=20, required=True)
    phone_number = forms.CharField(label='Contact Number', max_length=20)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email', 
            'username', 
            'password1', 
            'password2', 
            'street_address1', 
            'street_address2', 
            'county', 
            'town_or_city',
            'postcode',
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