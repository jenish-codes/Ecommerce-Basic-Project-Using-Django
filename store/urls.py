from django.urls import path

from store.views.home import index
from store.views.login import Login
from store.views.signup import Signup

urlpatterns = [
    path('', index, name= 'home'),
    path('signup', Signup.as_view()),
    path('login', Login.as_view()),
]
