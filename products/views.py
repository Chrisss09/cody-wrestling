from django.shortcuts import render, get_object_or_404
from .models import Product

def category(request):
    categories = Product.objects.all()
    return render(request, 'company.html', {'categories': categories})
    
def view_products(request):
    company_range = Product.objects.all()
    return render(request, 'products.html', {'company_range': company_range})

def view_more_info(request, slug_id):
    dvd_detail = Product.objects.filter(slug=slug_id)
    if dvd_detail.exists():
        dvd_detail = dvd_detail.first()
    else:
        return dvd_detail.DoesNotExist
    return render(request, 'dvdinfo.html', {'dvd': dvd_detail})