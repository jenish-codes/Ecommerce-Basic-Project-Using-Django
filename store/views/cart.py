from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View

from store.models import Customer
from store.models.product import Product


class Cart(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})
