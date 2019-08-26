# encoding: utf-8

# author    : liuzhanxiong
# email     : lzx1453536003@163.com
# IDE       : PyCharm
# time      : 2019-08-23 17:06

from django.urls import path
from . import views

app_name = "blog_app"

urlpatterns = [
    path(r"", views.HomePageView.as_view(), name = "home_page"),
    # path(r"category/<slug:category_name>", views.CategoryView.as_view(), name = "category"),
    # path(r"article_list/<str:{}>".format(), views.ArticleListView.as_view(), name = "article_list"),
]