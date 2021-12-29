from django.shortcuts import render
from product.models import Product,Cart


def product(request):
    products = Product.objects.all()

    context = {
        'products' : products,
    }

    return render(request, "product.html", context=context)


def cart(request):
    items = Cart.objects.all()

    context = {
        'items' : items,
    }

    return render(request, "cart.html", context=context)
