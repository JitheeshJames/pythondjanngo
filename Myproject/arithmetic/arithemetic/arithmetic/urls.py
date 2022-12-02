from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('submit/',views.submit, name='submit'),
    path('add/', views.add, name='add'),
    path('sub/', views.sub, name='sub'),
    path('mul/', views.mul, name='mul'),
    path('div/', views.div, name='div')
]
