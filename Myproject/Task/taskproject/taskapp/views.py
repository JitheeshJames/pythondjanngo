from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(requests):
    name='Jitheesh'
    return render(requests,'home.html', {'obj':name})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def details(request):
    return HttpResponse('This is the Details page')

def thanks(request):
    return HttpResponse('This is the Thanks page')