from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductView.as_view(), name="ProductView"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('buy/', views.buy_now, name='buy-now'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.search_page, name='search_result'),
    path('autosuggest/', views.auto_suggest, name='autosuggest'),
]
