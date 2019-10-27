from django.shortcuts import render
from .models import Product

def category(request):
    product = Product.objects.all()
    return render(request, 'company.html', {'product': product})
    