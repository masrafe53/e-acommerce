from django.shortcuts import render
from django.db.models import Q 
from django.shortcuts import render
from django.views import generic

from .models import Product
from .models import Category
from .models import slider






# Create your views here.

def home(request):
    my_product = Product.objects.filter(featured = True)
    my_category = Category.objects.filter(featured = True)
    my_slider = slider.objects.filter(show = True)
    


    diction = { 'my_product':my_product,'my_category':my_category,'my_slider':my_slider }
    return render(request,'home.html',context=diction)



class productpage(generic.DetailView):
    model = Product
    template_name = 'productpage.html'
    slug_url_kwarg = 'slug'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['related_products'] = self.get_object().related
        return context


class categoryproducts(generic.DeleteView):
    model = Category
    template_name = 'categoryproducts.html'
    slug_url_kwarg = 'slug'
    def get_context_data(self, **kwargs):

       context =  super().get_context_data(**kwargs)
       context['products'] = self.get_object().products.all()
       return context

class productlist(generic.ListView):
    model = Product
    template_name = 'productlist.html'
    context_object_name = 'productlist'
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class SearchResult(generic.View):
    def get(self,*args,**kwargs):
        key = self.request.GET.get('key', '')
        products = Product.objects.filter(
            Q(title__icontains = key)

        )
        context = {
            'products':products , 'key':key
        }
        return render(self.request,'search-result.html',context)