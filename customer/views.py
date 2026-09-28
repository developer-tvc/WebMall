from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import CustomerRegistrationForm

@login_required
def profile(request):
    return render(request, 'app/profile.html')

@login_required
def address(request):
    return render(request, 'app/address.html')


class SafeLogoutView(View):
    """Logout that validates the redirect target to prevent open redirects."""
    allowed_hosts = None  # set to ['yourdomain.com'] in production for stricter check

    def post(self, request, *args, **kwargs):
        next_url = request.POST.get('next') or request.GET.get('next') or '/'
        if not url_has_allowed_host_and_scheme(
            url=next_url,
            allowed_hosts=self.allowed_hosts or {request.get_host()},
            require_https=request.is_secure(),
        ):
            next_url = '/'
        auth_logout(request)
        return redirect(next_url)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

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
