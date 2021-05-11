from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    # return HttpResponse('this is polls page')
    return render(request, 'polls/homepage.html')
