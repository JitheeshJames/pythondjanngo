from django import forms
from .models import Movies
from django.forms import ModelForm

class MovieForm(forms.ModelForm):
    class Meta:
        model= Movies
        fields= ['name','desc','year','img']