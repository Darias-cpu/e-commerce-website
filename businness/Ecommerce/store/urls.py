from multiprocessing.resource_tracker import register
from tkinter.font import names

from django.urls import path
from . import views
from .views import collections
from store.controller import authview, cart

urlpatterns = [

    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('collections', views.collections, name='collections'),
    path('collections/<str:slug>', views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name='productview'),
    path('register/', authview.register, name='register'),# Add this line for the root URL
    path('login/', authview.loginpage, name='loginpage'),
    path('logout/', authview.logoutpage, name='logoutpage'),
    path('add-to-cart', cart.addtocart, name='addtocart'),
]
