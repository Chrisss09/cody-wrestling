from django.shortcuts import render
from .models import Product

def category(request):
    dvds = Product.objects.all()
    return render(request, 'company.html', {'dvds': dvds})
    