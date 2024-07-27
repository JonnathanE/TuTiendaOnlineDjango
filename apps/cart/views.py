from django.shortcuts import redirect, render

from apps.store.models import Product

from .cart import Cart

# Create your views here.


def add_product(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add_product(product)
    return redirect("cart:index")
