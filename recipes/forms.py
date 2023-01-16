from django import forms
from django.forms import ModelForm
from .models import Recipe

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter name...'}),
            'ingredients': forms.Textarea(attrs={'class':'form-control', 'placeholder':'enter ingredients...'})
        }