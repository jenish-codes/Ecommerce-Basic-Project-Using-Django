from django.urls import path

from store.views.cart import Cart
from store.views.home import Index
from store.views.login import Login, logout
from store.views.signup import Signup


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
]
