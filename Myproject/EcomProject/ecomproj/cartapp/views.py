from django.shortcuts import render, redirect, get_object_or_404
from ecom.models import Products
from .models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def _cart_id(requests):
    cart= requests.session.session_key
    if not cart:
        cart = requests.session.create()
    return cart

def add_cart(requests, id):
    product =Products.objects.get(id=id)

    try:
        cart = Cart.objects.get(cart_id =_cart_id(requests))

    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id =_cart_id(requests))
        product.stock -= 1
        product.save()
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        if cart_item.product.stock > 0:
            cart_item.quantity += 1
            product.stock -= 1
            if product.stock < 1:
                product.available = False
        cart_item.save()
        product.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product,cart=cart,quantity=1)
        cart_item.save()

    return redirect('cartapp:cart_details')

def cart_details(requests,total =0,counter=0,cart_items =None):

    try:
        cart = Cart.objects.get(cart_id=_cart_id(requests))
        cart_items = CartItem.objects.filter(cart=cart,active =True)
        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(requests,'cart.html',{'cart_items':cart_items,'total':total,'counter':counter})

def cart_remove(requests,product_id):
    cart = Cart.objects.get(cart_id = _cart_id(requests))
    product = get_object_or_404(Products,id=product_id)
    cart_item =CartItem.objects.get(product=product, cart= cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        product.stock += 1
        cart_item.save()
        if product.stock > 0:
            product.available = True
        product.save()
    else:
        cart_item.delete()

    return redirect('cartapp:cart_details')

def delete_cart(requests, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(requests))
    product = get_object_or_404(Products, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    product.stock += cart_item.quantity
    if product.stock > 0:
        product.available = True
    product.save()
    return redirect('cartapp:cart_details')