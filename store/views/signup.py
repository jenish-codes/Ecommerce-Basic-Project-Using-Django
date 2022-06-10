from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

from store.models import Customer



class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):

        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # Validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        # Saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = 'First Name Required!'
        elif len(customer.first_name) < 4:
            error_message = 'First name must be above 4 charecters'
        elif not customer.last_name:
            error_message = 'Last name required'
        elif len(customer.last_name) < 4:
            error_message = 'Last name must be above 4 charecters'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Enter a valid Mobile Number'
        elif not customer.email:
            error_message = 'Phone Number required'
        elif len(customer.email) < 5:
            error_message = 'Enter a valid Email ID'
        elif not customer.password:
            error_message = 'Password Cannot be Blank'
        elif len(customer.password) < 6:
            error_message = 'Password must be above six charecters'

        elif customer.isExists():
            error_message = 'Email Address already Registered'
        return error_message
