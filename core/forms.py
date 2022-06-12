from django import forms
from .models import *
from django.forms import ModelForm


class TaskForm(forms.ModelForm):

    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

    class Meta:
        model = Task
        # fields = '__all__'
        exclude = ['completed_to', 'completed', 'user']