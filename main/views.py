from django.shortcuts import render

from .models import Product

# Create your views here.
def index(request):                                                        
    return render(request, "main/home.html")

def products(request):
    products = Product.objects.all() 
    return render(request, "main/product.html", {"products":products})