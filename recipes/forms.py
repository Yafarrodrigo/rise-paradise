from django import forms
from django.forms import ModelForm
from .models import Recipe
from django.core.exceptions import ValidationError


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'preparation', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter name...'}),
            'ingredients': forms.Textarea(attrs={'class':'form-control', 'placeholder':'enter ingredients...'})
        }

    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('photo'):
            raise ValidationError('solo imagenes!')

        return self.cleaned_data


class RecipeFormEdit(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'preparation']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter name...'}),
            'ingredients': forms.Textarea(attrs={'class':'form-control', 'placeholder':'enter ingredients...'})
        }