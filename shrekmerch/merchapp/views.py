from django.shortcuts import render
from .models import Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'merchapp/all_products.html', {'products': products})


