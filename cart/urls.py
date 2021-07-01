from django.urls import path
from . import views
from . import apps

app_name = 'cart'

urlpatterns = [
    path('',views.add_to_cart, name='add-to-cart'),
    path('show-cart/',views.show_cart, name='show-cart'),

]