from django.forms.models import model_to_dict
from django.urls import path
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import models
from django import forms
from django.forms import formset_factory
from django.forms import modelformset_factory, inlineformset_factory


class Country(models.Model):
    name = models.CharField(max_length=30)
    
class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


def formset_view(request,country_id):
    country_obj = Country.objects.get(pk=country_id)
   
    cityFormSet = inlineformset_factory(Country, City,fields=('name',), extra = 3)

    if request.method =="POST":
        formset = cityFormSet(request.POST or None, instance = country_obj)        
        
        if formset.is_valid():
            formset.save()      
                
            return HttpResponse("done")
              
    # Add the formset to context dictionary
    new_formset = cityFormSet(queryset=City.objects.none())
    context= {'formset': new_formset, 'country_obj': country_obj}
    return render(request, "index.html", context)


def index(request):
    return HttpResponse("all")

urlpatterns = [
    path('home/', index),
    path('form/<int:country_id>', formset_view),
 
]