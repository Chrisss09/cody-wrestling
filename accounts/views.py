from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm

def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('home'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have logged out successfully')
    return redirect(reverse('home'))