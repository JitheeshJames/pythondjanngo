from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Products
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.

# def index(requests):
#     return HttpResponse("Hi")

def allProdCat(requests, c_slug=None):
    c_page = None
    products_list = []
    if c_slug !=None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Products.objects.all().filter(category=c_page, available=True)
    else:
        products_list = Products.objects.all().filter(available=True)

    paginator = Paginator(products_list,8)

    try:
        page = int(requests.GET.get('page',1))

    except:
        page = 1

    try:
        products = paginator.page(page)

    except(EmptyPage,InvalidPage):

        products= paginator.page(paginator.num_pages)


    return render(requests,'category.html',{'category':c_page,'products':products})

def ProdDetails(requests,c_slug,p_slug):
    try:
        product = Products.objects.get(category__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e
    return render(requests,'product.html',{'product':product})