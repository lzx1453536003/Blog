# encoding: utf-8

# author    : liuzhanxiong
# email     : lzx1453536003@163.com
# IDE       : PyCharm
# time      : 2019-08-23 17:06

from django.urls import path
from . import views

app_name = "blog_app"

urlpatterns = [
    path(r"", views.HomePageView.as_view()),
    path(r"category_detial/<slug:category_name>", views.CategoryDetialView.as_view(), name = "category_detial"),
    # path(r"article_list/<str:{}>".format(), views.ArticleListView.as_view(), name = "article_list"),
]