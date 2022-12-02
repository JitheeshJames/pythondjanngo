from django.urls import path
from . import views

app_name='cartapp'

urlpatterns = [
    path('',views.cart_details,name='cart_details'),
    path('add/<int:id>/',views.add_cart, name='add_cart'),
    path('delete/<int:product_id>/',views.cart_remove, name='cart_remove'),
    path('remove/<int:product_id>/',views.delete_cart, name='delete_cart'),
]