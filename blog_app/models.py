from django.db import models
from django.urls import reverse
from uuslug import slugify

class Category(models.Model):
    """
    文章类别
    """
    name = models.CharField(verbose_name='类别名称', max_length=30, unique=True)
    parent_category = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name='父类别名称')
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = '类别'
        verbose_name = '分类'

    def get_absolute_url(self):
        return reverse("blog_app:category_detial", kwargs={'category_name':self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Article(models.Model):
    title = models.CharField('title', max_length=200, unique=True)
    summary = models.CharField('summary', max_length=2000)
    body = models.TextField('body')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=False, null=False)


def get_category_tree(category = None):
    category_tree = {}
    categorys = Category.objects.all()
    sub_categorys = categorys.filter(parent_category=category)
    for category in sub_categorys:
        category_tree[category] = {}
    for key, value in category_tree.items():
        category_tree[key] = get_category_tree(key)
    return category_tree