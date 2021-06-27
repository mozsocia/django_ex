from django.forms.models import model_to_dict
from django.urls import path
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import models

from django.shortcuts import render
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})


def index(request):
    return HttpResponse("all")

urlpatterns = [
    path('home/', home),
]