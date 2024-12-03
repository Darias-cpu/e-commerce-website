from django.shortcuts import render, redirect
from django.contrib import messages

from store.models import Category, Product



# Create your views here.
def home(request):
    return render(request, 'store/index.html')

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, "store/collections.html", context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category_name': category}
        return render(request, "store/products/index.html", context)
    else:
        messages.warning(request, 'Category does not exist')
        return redirect('collections')

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products': products}
        else:
            messsages.error(request, 'Product does not exist')
            return redirect('collections')




    else:
        messsages.error(request, 'Category does not exist')
        return redirect('collections')
    return render(request, "store/products/view.html", context)