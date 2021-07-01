from django.shortcuts import render,redirect
from product.models import Product
from .models import Cart
from django.db.models import Q
from django.http import JsonResponse

def add_to_cart(request):
    user = request.user
    if request.GET.get('prod_id'):
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        Cart(user=user,product=product).save()
    return redirect('/show-cart')


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount =0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product =[p for p in Cart.objects.all() if p.user == user]
        if  cart_product:
            for p in cart_product:
                temp_amount = (p.quantity* p.product.discounted_price)
                amount+= temp_amount
                total_amount = amount +shipping_amount
            return render(request, 'app/add_to_cart.html',{'carts':cart,'total_amount':total_amount,'amount':amount})
        else:
            return render(request,'app/emptycart.html')



def plus_cart(request):
    if request.method =='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==request.user]
        for p in cart_product:
            temp_amount = (p.quantity * p.product.discounted_price)
            amount += temp_amount
            total_amount = amount + shipping_amount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': total_amount
        }
        return JsonResponse(data)



