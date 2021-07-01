from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .helper import send_mail_without_celery
from .models import Product


class ProductView(View):
    def get(self, request):
        # send_mail_without_celery()
        sarees = Product.objects.filter(category='S')
        casual_shirt = Product.objects.filter(category='C')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        return render(request, 'app/home.html',
                      {'sarees': sarees, 'casual_shirt': casual_shirt, 'mobiles': mobiles, \
                       'laptops': laptops})


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/product_detail.html', {'product': product})




def buy_now(request):
    return render(request, 'app/buy_now.html')


def orders(request):
    return render(request, 'app/orders.html')


def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'Samsung' or data == 'Apple':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(selling_price__lte=10000)
    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(selling_price__gte=10000)
    return render(request, 'app/product_list.html', {'mobiles': mobiles})


def checkout(request):
    return render(request, 'app/check_out.html')


def search_page(request):
    srh = request.GET.get('search')
    product = Product.objects.filter(title__icontains=srh)
    return render(request, 'app/search.html', {'product': product})


def auto_suggest(request):
    print(request.GET)
    query_original = request.GET.get('term')
    queryset = Product.objects.filter(title__contains=query_original)
    list = []
    list += [x.title for x in queryset]
    return JsonResponse(list, safe=False)


