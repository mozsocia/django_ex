from django.forms.models import model_to_dict
from django.forms.widgets import TextInput
from django.urls import path
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import models
from django.db import models
from django import forms


class RawProductForm(forms.Form):
    title = forms.CharField(label="Title", required=True,
                            widget=forms.TextInput())
    
    description = forms.CharField(
        required=True, widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "my-form-id",
                "rows": 10,
                "cols" : 20
            }
        )
    )
    
    user_dob = forms.DateField(
        label="Date of Birth", widget=forms. TextInput(attrs={'type': 'date'}))

    user_email = forms. EmailField(label="Email", widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Email Address', }))

    boolean_field = forms.BooleanField(required=False)

    field = forms.ChoiceField(
        choices=(('1', 'First'), ('2', 'Second'), ('3', 'Third')))

    choices = (('', '--SELECT OPTION--'), ('1', 'First'),
               ('2', 'Second'), ('3', 'Third'))
    field22 = forms.ChoiceField(choices=choices)

    choices = (('A', 'A'), ('B', 'B'), ('C', 'C'))
    field33 = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)

    choices = (('', '--SELECT OPTION--'), ('1', 'First'),
               ('2', 'Second'), ('3', 'Third'))
    field44 = forms.MultipleChoiceField(choices=choices, required=False)

    choices = (('A', 'A'), ('B', 'B'), ('C', 'C'))
    field55 = forms. MultipleChoiceField(
        choices=choices, widget=forms.CheckboxSelectMultiple)
    
    
    
    
''' queryset in form field 
----------------------------------------------------------------------'''

class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    aaa = models.CharField(max_length=200)
    bbb = models.CharField(max_length=200)
 
    def __str__(self):
        return self.choice_text



class Contatto(models.Model):
    contatto_choice =  models.ForeignKey(Choice, on_delete=models.PROTECT)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.email
    
    
class ContactForm(forms.ModelForm):    
    contatto_choice = forms.ModelChoiceField(queryset=Choice.objects.filter(id__in=[1, 3, 4]),widget=forms.RadioSelect)
    class Meta:
        model = Contatto
        fields = ['contatto_choice','email','name']
        
        
        

''' all views 
-----------------------------------------------------------------------'''
def index(request):
    return HttpResponse("all")

def form_fn(request):
    newform = RawProductForm()
    contxt= {"l_form": newform}
    return render(request, 'index.html', contxt)

def form_fn2(request):
    print(Choice.objects.all())
    newform = ContactForm()
    contxt= {"l_form": newform}
    return render(request, 'index.html', contxt)

def create_fn(request):
    Choice.objects.create(choice_text="dfskjadskf one" , aaa="aaa one", bbb="bbb one" )
    Choice.objects.create(choice_text="dfskjadskf two" , aaa="aaa two", bbb="bbb two" )
    Choice.objects.create(choice_text="dfskjadskf three" , aaa="aaa three", bbb="bbb three" )
    Choice.objects.create(choice_text="dfskjadskf four" , aaa="aaa four", bbb="bbb four" )
    
    return HttpResponse("done")

urlpatterns = [
    path('home/', index),
    path('form/',form_fn),
    path('form2/', form_fn2),
    path('create/', create_fn)
]
