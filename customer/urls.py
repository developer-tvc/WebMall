"""WebMall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name ='password_reset'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),
         name='login'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('password-change/',
         auth_views.PasswordChangeView.as_view(template_name='app/password_change.html',
                                               form_class=MyPasswordChangeForm,
                                               success_url='/password-change-done/'), name='passwordchange'),
    path('password-change-done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='app/password_change_done.html'),
         name='password-change-done'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),
         name='password_reset_complete'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('signup/', views.signup, name="signup"),
]
