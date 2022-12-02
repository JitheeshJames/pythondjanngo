from django.urls import path
from . import views

app_name='regloginapp'

urlpatterns = [
    path('',views.signup,name='signup'),
    path('register',views.signup,name='register'),
]