# from django.contrib import admin
from django.urls import path

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db import models
from rest_framework.serializers import ModelSerializer


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


''' ---------------------------------------
all necessary fucntions for view is below'''


@api_view(['GET'])
def index(request):
    posts = Post.objects.all()
    serialPosts = PostSerializer(posts, many=True)

    return Response(serialPosts.data)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/', index)


]
