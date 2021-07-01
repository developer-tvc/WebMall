from django.shortcuts import render
from product.models import Product
from .models import Cart

def add_to_cart(request):
    user = request.user
    if request.GET.get('prod_id'):
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        Cart(user=user,product=product).save()
    return render(request, 'app/add_to_cart.html')


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        return render(request, 'app/add_to_cart.html',{'carts':cart})