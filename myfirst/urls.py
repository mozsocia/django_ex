
from django.contrib import admin

from django.urls import path
from django.shortcuts import render
from django.urls.conf import include


def index(request):
    return render(request, 'myfirst/homepage.html')


def about(request):
    return render(request, 'myfirst/about.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('polls/', include('apps.polls.urls')),
    path('newapp/', include('apps.newapp.urls'))
]
