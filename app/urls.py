from django.urls import path
from .views import productpage
from .views import categoryproducts
from .views import productlist
from .views import SearchResult
from .views import home
from . import views

urlpatterns = [ 
    path('',views.home,name = 'home'),
    path('product-page/<str:slug>/', productpage.as_view(), name = 'productpage'),
    path('categoryproducts/<str:slug>/', categoryproducts.as_view(), name = 'categoryproducts'),
    path('productlist',productlist.as_view(),name='productlist'),
    path('search-result',SearchResult.as_view(),name = 'search-result')
]



