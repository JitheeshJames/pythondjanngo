from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def add(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    res = num1 + num2
    return render(request, 'add.html',{'add':res})

def sub(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    res = num1 - num2
    return render(request, 'sub.html',{'sub':res})

def mul(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    res = num1 * num2
    return render(request, 'mul.html',{'mul':res})

def div(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    res = num1 / num2
    return render(request, 'div.html',{'div':res})

def submit(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    divi = num1 / num2
    multi = num1 * num2
    subs = num1 - num2
    addi = num1 + num2
    return render(request, 'submit.html',{'div':divi,'mul':multi,'add':addi,'sub':subs})