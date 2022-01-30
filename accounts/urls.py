from re import template
from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/',views.register, name="register"),
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),

    path('',views.home, name="home"), 
    
    path('user-page/',views.user_page, name="user_page"),
    path('account-settings/',views.account_settings, name="account_settings"),

    path('products/',views.products,name="products"),
    path('create-products/',views.create_products,name="create_products"),

    path('customer/<str:pk>/',views.customer,name="customer"),
    path('update-customer/<str:pk>/',views.update_customer,name="update_customer"),

    path('create-order/',views.create_order,name="create_order"),
    path('create-single-order/<str:pk>/',views.create_single_order,name="create_single_order"),
    path('update-order/<str:pk>/',views.update_order,name="update_order"),
    path('delete-order/<str:pk>/',views.delete_order,name="delete_order"),

    path('reset-password/',
        auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
        name="reset_password"),
    path('reset-password-sent/',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),
        name='password_reset_confirm'),
    path('reset-password-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),
        name='password_reset_complete'),

]