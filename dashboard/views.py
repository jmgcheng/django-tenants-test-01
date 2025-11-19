from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, "dashboard/home.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, "dashboard/products.html", {"products": products})
