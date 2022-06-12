from django.urls import path

from store.views.cart import Cart
from store.views.home import Index
from store.views.login import Login, logout
from store.views.signup import Signup
from store.views.checkout import CheckOut
from store.views.orders import OrderView


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', OrderView.as_view(), name='orders'),
]
