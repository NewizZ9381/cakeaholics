from django.shortcuts import render,get_object_or_404
from store.models import Category,Product
# from django.http import HttpResponse

# Create your views here.
def index(request,category_slug=None):
    products=None
    category_page=None
    if category_slug!=None:
        category_page=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.all().filter(category=category_page,available=True)
    else :
        products=Product.objects.all().filter(available=True)

    return render(request, 'index.html',{'products':products,'category':category_page})

def productPage(request,category_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html',{'product':product})