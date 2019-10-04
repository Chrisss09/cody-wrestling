from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

def login(request):
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have logged out successfully')
    return redirect(reverse('home'))