from django.forms.models import model_to_dict
from django.urls import path
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import models
from django import forms
from django.forms import formset_factory
from django.forms import modelformset_factory


class Geek(models.Model):
    title =models.CharField(max_length=30)
    description = models.CharField(max_length=30)


def formset_view(request):
  

  
    # creating a formset and 3 instances of GeeksForm
    GeeksFormSet = modelformset_factory(Geek,fields=('title', 'description'), extra = 3)
    # GeeksFormSet = modelformset_factory(Geek,exclude=(), extra = 3)  # for include all
    if request.method =="POST":
        formset = GeeksFormSet(request.POST or None)        
        # print formset data if it is valid
        if formset.is_valid():
            formset.save()
              
    # Add the formset to context dictionary
    new_formset = GeeksFormSet(queryset=Geek.objects.none())
    context= {'formset': new_formset}
    return render(request, "index.html", context)


def index(request):
    return HttpResponse("all")

urlpatterns = [
    path('home/', index),
    path('form/', formset_view)
]