from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
