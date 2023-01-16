from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        data = {
                'form': UserCreationForm
            }
        return render(request, 'signup.html', data)
    else:
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                user = User.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('todo ok')

            except:
                return HttpResponse('todo mal')
                
        else:
            return HttpResponse('todo mal')