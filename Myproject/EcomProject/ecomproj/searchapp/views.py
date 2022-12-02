from django.shortcuts import render
from ecom.models import Products
from django.db.models import Q


# Create your views here.

def searchresults(requests):
    products =None
    query =None
    if 'q' in requests.GET:
        query = requests.GET.get('q')
        products = Products.objects.all().filter(Q(name__contains = query) | Q(desc__contains = query))

        return render(requests,'search.html',{'query':query,'products':products})
