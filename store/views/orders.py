from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View

from store.models import Customer
from store.models.product import Product
from store.models.orders import Order

class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'orders.html', {'orders': orders})
