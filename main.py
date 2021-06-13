# from django.contrib import admin

from django.http.response import HttpResponse
from django.urls import path
from django.http import JsonResponse
from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)


''' ---------------------------------------
all necessary fucntions for view is below'''


def index_single_obj(request):
    obj = Posts.objects.filter(pk=10).values()
    data = list(obj)
    return JsonResponse(data, safe=False)

#path('home/', index)


def index(request):
    obj = Posts.objects.all().values()
    data = list(obj)
    return JsonResponse(data, safe=False)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/', index),
    path('sin/', index_single_obj)
]
