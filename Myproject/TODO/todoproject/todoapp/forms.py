from .models import Task
from django import forms

class TaskForms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','desc','priority','date']