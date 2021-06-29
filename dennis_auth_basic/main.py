from django.forms.models import model_to_dict
from django.urls import path
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
    

@login_required(login_url='login')
def home(request):
    print(request.user.is_authenticated)
    return render(request, 'home.html', context={})

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html', context={})

@login_required(login_url='login')
def product(request):    
    return render(request, 'product.html', context={})


def registerPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"account created for " + user )
            return redirect('register')
    else: 
        form = CreateUserForm()    
              
    context = {"form": form}
    return render(request, 'register.html', context)


def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            messages.error(request,"invalid username or password")
            return redirect('login')
        else:            
            login(request, user)            
            messages.success(request,"account logged in for " + user.get_username())
            return redirect('home')
        
        
    
    form = AuthenticationForm()
    context = {"form": form}
    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

urlpatterns = [
    path('home/', home, name='home'),
    path('index/', index),
    path('product/', product),
    path('register/', registerPage, name = 'register'),
    path('login/', loginPage, name= "login"),
    path('logout/', logoutPage, name= "logout"),
    
]