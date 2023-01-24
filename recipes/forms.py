from django import forms
from django.forms import ModelForm
from .models import Recipe, Profile
from django.core.exceptions import ValidationError


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name','description', 'ingredients', 'preparation', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'enter name...'}),
            'description': forms.Textarea(attrs={'class':'form-control my-2', 'placeholder':'enter short description...'}),
            'ingredients': forms.Textarea(attrs={'class':'form-control my-2', 'placeholder':'enter ingredients...'}),
            'preparation': forms.Textarea(attrs={'class':'form-control my-2', 'placeholder':'describe how to prepare...'}),
            'photo': forms.FileInput(attrs={'class':'form-control my-2', 'onchange': 'loadFile(event);'})
        }

    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('photo'):
            raise ValidationError('solo imagenes!')

        return self.cleaned_data

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname','bio','email','photo']
        widgets = {
            'nickname': forms.TextInput(attrs={'class':'form-control my-2'}),
            'bio': forms.Textarea(attrs={'class':'form-control my-2'}),
            'email': forms.EmailInput(attrs={'class':'form-control my-2', 'required':False}),
            'photo': forms.FileInput(attrs={'class':'form-control my-2', 'onchange': 'loadFile(event);'})
        }

class RecipeFormEdit(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'ingredients', 'preparation']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'enter name...'}),
            'description': forms.Textarea(attrs={'class':'form-control my-2', 'placeholder':'enter short description...'}),
            'ingredients': forms.Textarea(attrs={'class':'form-control my-2', 'placeholder':'enter ingredients...'}),
            'preparation': forms.Textarea(attrs={'class':'form-control my-2', 'placeholder':'describe how to prepare...'})
        }