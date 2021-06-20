# from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path
from django.http import JsonResponse
from django.db import models
from django.forms.models import model_to_dict


class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)


''' ---------------------------------------
all necessary fucntions for view is below'''


def index_single_obj2(request):
    obj = Posts.objects.filter(pk=1).values()
    data = obj[0]
    return JsonResponse(data, safe=False)


def index_single_obj(request):
    new = Posts.objects.get(pk=1)
    obj = new
    return JsonResponse(model_to_dict(obj))

#path('home/', index)


def index(request):
    new = Posts.objects.all().values()
    obj = new
    return JsonResponse(list(obj.values()), safe=False)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/', index),
    path('sin/', index_single_obj),
    path('sin2/', index_single_obj2)
]
