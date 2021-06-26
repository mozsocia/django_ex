from django.urls import path
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import models
from django import forms
from django.forms import formset_factory


''' all models
-----------------------------------------------------------'''
class Geek(models.Model):
    title =models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    

class GeeksForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    

''' all views
-----------------------------------------------------------'''
def formset_view(request):
  
    context ={}
  
    # creating a formset and 3 instances of GeeksForm
    GeeksFormSet = formset_factory(GeeksForm, extra = 3)
    formset = GeeksFormSet(request.POST or None)
      
    # print formset data if it is valid
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)      
                  
            Geek.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'))
              
    # Add the formset to context dictionary
    context['formset']= formset
    return render(request, "index.html", context)


def index(request):
    return HttpResponse("all")

urlpatterns = [
    path('home/', index),
    path('form/', formset_view)
]



''' all html
-----------------------------------------------------------'''
'''
<form method="POST" enctype="multipart/form-data">

    {{ formset.management_data }}
    {% csrf_token %}
    {{ formset.as_p }}
    <input type="submit" value="Submit">
</form>
'''
