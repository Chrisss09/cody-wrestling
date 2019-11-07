from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q
from django.core.paginator import Paginator

def category(request):
    categories = Product.objects.all()
    return render(request, 'company.html', {'categories': categories})


def view_products(request, category):
    dvds = Product.objects.filter(Q(category__icontains=category))
    context = {
        'object_list': dvds,
        'category': category
    }
    return render(request, 'products.html', context)

# def view_more_info(request, slug_id):
#     dvd_detail = Product.objects.filter(slug=slug_id)
#     if dvd_detail.exists():
#         dvd_detail = dvd_detail.first()
#     else:
#         return dvd_detail.DoesNotExist
#     return render(request, 'dvdinfo.html', {'dvd': dvd_detail})