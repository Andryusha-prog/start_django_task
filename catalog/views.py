from django.shortcuts import render

from catalog.models import Product


# Create your views here.

def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def single_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'single_product.html', context)


def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products.html', context)

