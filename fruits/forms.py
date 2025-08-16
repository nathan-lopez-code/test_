from django import forms
from django.forms import widgets

from fruits.models import Fruit


class CreateFruit(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'description', 'image']
