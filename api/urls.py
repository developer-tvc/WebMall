from django.urls import path, include
from knox import views as knox_views
from . import views
from .views import RegisterAPI

urlpatterns = [
    path('product/', views.ProductSerializerView.as_view()),
    path('register/', RegisterAPI.as_view(), name='api-register'),
    path('login/', views.LoginAPI.as_view(), name='api-login'),
    path('logout/', knox_views.LogoutView.as_view(), name='api-logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='api-logoutall'),
    path('change-password/', views.ChangePasswordView.as_view(), name='api-change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='api-password_reset')),
]
