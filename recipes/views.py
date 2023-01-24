from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, RecipeFormEdit, ProfileForm
from .models import Recipe, Profile
import cloudinary

import json


# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
                'form': AuthenticationForm
            })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': "Datos incorrectos"
            })
        else:
            login(request, user)
            return redirect('recipes')
        
def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
                'form': UserCreationForm
            })
    else:
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                profile = Profile.objects.create(user=user, bio="No bio added",nickname=request.POST['username'])
                user.save()
                profile.save()
                login(request, user)
                editForm = ProfileForm(instance=request.user.profile)
                return render(request, 'edit_profile.html', {
                    'profileSetup': True,
                    'form': editForm
                })

            except IntegrityError:
                return render(request, 'signup.html',{
                    'form': UserCreationForm,
                    'error': "el usuario ya existe"
                })                
        else:
            return render(request, 'signup.html',{
                    'form': UserCreationForm,
                    'error': "las contraseñas no coinciden"
                }) 

@login_required
def createRecipe(request):
    if request.method == 'GET':
        return render(request, 'create_recipe.html',{
        'form': RecipeForm
    })
    else:
        try:
            form = RecipeForm(request.POST, request.FILES)
            newRecipe = form.save(commit=False)
            newRecipe.user = request.user
            newRecipe.save()

            return redirect('recipes')

        except Exception as e:
            return render(request, 'create_recipe.html',{
                'form': RecipeForm,
                'error': e
            })

def recipes(request):
    search_value = " "
    if request.method == 'GET':
        if 'search' in request.GET:
            try:
                search_value = request.GET['search']
                multiple_q = Q(
                    Q(name__icontains=search_value) |
                    Q(description__icontains=search_value) |
                    Q(ingredients__icontains=search_value) |
                    Q(user__profile__nickname__icontains=search_value) |
                    Q(user__username__icontains=search_value)
                )
                recipes = Recipe.objects.filter(multiple_q)
            except:
                recipes = Recipe.objects.all()
        else:
            recipes = Recipe.objects.all()

    return render(request, 'recipes.html',{
        'recipes': recipes,
        'search_value': search_value
    })

@login_required
def detailRecipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'detail_recipe.html',{
        'recipe': recipe
    })

@login_required
def editRecipe(request, recipe_id):
    if request.method == 'GET':
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        form = RecipeForm(instance=recipe)
        return render(request,'edit_recipe.html',{
            'form': form,
            'recipe': recipe
        })
    else:
        try:
            recipe = get_object_or_404(Recipe, pk=recipe_id)
            if recipe.user == request.user:
                form = RecipeForm(request.POST, request.FILES, instance=recipe)
                if 'photo' in request.FILES:
                    cloudinary.uploader.destroy(str(recipe.photo))

                form.save()
                return redirect('recipes')
            else:
                return render(request,'edit_recipe.html',{
                'form': form,
                'recipe': recipe,
                'error': "not allowed!"
            })
        except Exception as e:
            print(e)
            return redirect('recipes')

@login_required
def deleteRecipe(request, recipe_id):

    if request.method == "GET":
        try:
            recipe = get_object_or_404(Recipe, pk=recipe_id)
            if recipe.user == request.user:
                cloudinary.uploader.destroy(str(recipe.photo))
                recipe.delete()
                return redirect('recipes')
        except:
            return redirect('recipes')

@login_required
def ownProfilePage(request):
    data = Profile.objects.all()
    ownRecipes = Recipe.objects.filter(user=request.user)
    return render(request, 'own_profile.html',{
        'data': data[0],
        'recipes': ownRecipes
    })

@login_required
def profilePage(request, userId):
    queryUser = User.objects.get(pk=userId)
    userRecipes = Recipe.objects.filter(user=queryUser)
    return render(request, 'profile.html',{
        'userProfile':queryUser,
        'recipes':userRecipes
    })

@login_required
def editProfile(request):
    
    if request.method == "GET":
        form = ProfileForm(instance=request.user.profile)
        return render(request, 'edit_profile.html', {
            'form': form
        })
    else:
        try:
            form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
            newData = form.save(commit=False)
            newData.user = request.user
            newData.save()
            return redirect('ownProfile')
        except Exception as e:
            print(e)
            form = ProfileForm(instance=request.user.profile)
            return render(request, 'edit_profile.html', {
                'form': form
            })

def searchRecipe(request):
    if request.method == 'POST':
        recipes = Recipe.objects.all()
        return render(request, 'recipes',{
            'recipes': recipes
        })