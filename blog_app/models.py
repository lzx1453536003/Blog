from django.db import models
from django.urls import reverse

class Category(models.Model):
    """
    文章类别
    """
    name = models.CharField('name', max_length=30, unique=True)
    parent_category = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse("")



# class NavigationTag(models.Model):
#
#     tag_name = models.CharField(max_length = 30)
#
#     def get_absolute_url(self):
#         return reverse("blog_app:article_list", kwargs={"article_type" : self.tag_name})

# class Article(models.Model):
#     title   = models.CharField(max_length = 30)
#     summary = models.CharField(max_length = 100)
#     content = models.CharField(max_length = 300)
#     author  = models.CharField(max_length = 30)

    # article_type =

