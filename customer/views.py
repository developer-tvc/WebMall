from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .forms import CustomerRegistrationForm


def profile(request):
    return render(request, 'app/profile.html')


def address(request):
    return render(request, 'app/address.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customer_registration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registered successfully')
            form.save()
        return render(request, 'app/home.html')

# Create your views here.
