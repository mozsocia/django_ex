from django.urls import path
from django.http.response import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from app.models import *
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


''' 
jodi settings.py

TIME_ZONE = 'Asia/Dhaka'
USE_TZ = True

than " timezone.now " will output utc time
so use this method to output local time

>>> from django.utils import timezone
>>> timezone.localtime(timezone.now())

jodi 
USE_TZ = False
than "timezone.now" will output localtime

'''

''' ---------------------------------------
all necessary fucntions for view is below'''


def index_single_obj(request):
    pass
    # obj = Employee.objects.get(name='Simpson').department
    # data1 = model_to_dict(obj)
    # return JsonResponse(data1)


def multi(request):
    pass
    # new = Employee.objects.get(name='Simpson').department
    # obj = Employee.objects.filter(department=new).values()
    # data = list(obj)
    # return JsonResponse(data, safe=False)


def create(request):
    Person.objects.create(name="mozdatwo", age=12)
    return HttpResponse("done")


def showall(request):
    new = Person.objects.all().values()
    return JsonResponse(list(new), safe=False)


urlpatterns = [
    path('create/', create),
    path('showall/', showall)

]
