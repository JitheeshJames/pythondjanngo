from django.urls import path
from . import views

app_name='ecom'

urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.ProdDetails,name='product_details'),
]