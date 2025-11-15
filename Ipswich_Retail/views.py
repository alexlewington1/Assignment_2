from django.shortcuts import render
from .forms import ProductForm
from .models import Product


def LandingPage(response):
    return render(response,"LandingPage.html")
def ProductPage(response):
    return render(response,"ProductPage.html")
def AboutUs(response):
    return render(response,"AboutUs.html")
def ContactUs(response):
    return render(response,"ContactUs.html")

def products_view(request):
    products = Product.objects.all()
    return render(request, "ProductPage.html", {"products": products})