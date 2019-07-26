from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField('标题', max_length=200, unique=True)
    body = models.CharField('正文', max_length=200, unique=True)