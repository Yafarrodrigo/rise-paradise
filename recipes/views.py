from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render


# Create your views here.
def helloworld(request):
    return render(request, 'home.html')

def signout(request):
    logout(request)
    return redirect('home')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
                'form': UserCreationForm
            })
    else:
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                user = User.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')

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

def recipes(request):
    return render(request, 'recipes.html')