from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404,redirect
from .carts import Cart
from app.models import Product
# Create your views here.


class AddToCart(generic.View):
    def post(self,*args,**kwargs):
        product = get_object_or_404(Product,id = kwargs.get('product_id'))
        cart = Cart(self.request)
        cart.update(product.id,1)
        return redirect('productpage',slug = product.slug)


class CartItem(generic.TemplateView):
    template_name = 'cart_page.html'