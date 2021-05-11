from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('new app')
    return render(request, 'newapp/homepage.html')
