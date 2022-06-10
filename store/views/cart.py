from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View

from store.models import Customer


class Cart(View):
    def get(self, request):
        return render(request, 'cart.html')

