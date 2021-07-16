from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.decorators import *
from django.contrib.auth.models import Group
from app.models import *
from django import forms
from django.core.exceptions import ObjectDoesNotExist



class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields ='__all__'
		exclude = ['user']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields =['username', 'email', 'password1', 'password2']
	
'''Normal page views
-----------------------------------------------------------------------------'''

@login_required(login_url='login_ep')
def homePage(request):
	return render(request, 'home.html', context={})

@login_required(login_url='login_ep')
def indexPage(request):
	return render(request, 'index.html', context={})


@allowed_group2(allowed=['admin'])
@login_required(login_url='login_ep')
def productPage(request):    
	return render(request, 'product.html', context={})



def userPage(request):
	

	try:
		
		customer_obj = request.user.customer
		user_orders = customer_obj.order_set.all()
		form = CustomerForm(instance=customer_obj)
		is_customer = True
  
	except ObjectDoesNotExist:
		user_orders = None
		form = CustomerForm()
		is_customer = False

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer_obj)
		if form.is_valid():
			form.save()
   
	context = {'orders': user_orders,'form':form, 'is_customer':is_customer}
	return render(request, 'user.html',context)

'''login logout page views
-------------------------------------------------------------'''
@login_check
def registerPage(request):
	
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			
			group = Group.objects.get(name='customer')
			user.groups.add(group)
   
			Customer.objects.create(
				user=user,
				name=user.username,
				)
			
			messages.success(request,"account created for " + user.username)
			return redirect('login_ep')
	else: 
		form = CreateUserForm()    
			  
	context = {"form": form}
	return render(request, 'register.html', context)

@login_check
def loginPage(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(request, username=username, password=password)
		
		if user is None:
			messages.error(request,"invalid username or password")
			return redirect('login_ep')
		else:            
			login(request, user)            
			messages.success(request,"account logged in for " + user.get_username())
			return redirect('user_ep')
		
		
	
	form = AuthenticationForm()
	context = {"form": form}
	return render(request, 'login.html', context)

def logoutPage(request):
	logout(request)
	return redirect('login_ep')



urlpatterns = [
	path('home2/', homePage, name='home_ep'),
	path('index/', indexPage),
	path('product/', productPage),
	path('register/', registerPage, name = 'register_ep'),
	path('login/', loginPage, name= "login_ep"),
	path('logout/', logoutPage, name= "logout_ep"),
	path('user', userPage, name= "user_ep")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


