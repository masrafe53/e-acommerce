from django.urls import path
from .views import AddToCart , CartItem

urlpatterns = [
    path('cart_page/',CartItem.as_view(),name='cart_page'),
    path('add-to-cart/<int:product_id>/',AddToCart.as_view(),name='add-to-cart'),
    



]