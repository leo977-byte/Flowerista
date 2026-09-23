from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product_detail, name='product_detail_default'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('custom-flower/', views.create_flower_view, name='create_flower'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
]