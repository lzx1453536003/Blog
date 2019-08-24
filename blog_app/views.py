from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
# from .models import Publisher, Book
from django.conf import settings
from django.core import cache
from django.views.generic.base import View

from .models import NavigationTag, Article

import logging

logger = logging.getLogger(__name__)


class IndexView(ListView):
    '''
    导航栏目view
    '''
    model = NavigationTag;
    template_name = "blog_app/index.html"
    context_object_name = "navigationtag_list"

    # def get_context_data(self, **kwargs):
    #     super().get_context_data(**kwargs);

class ArticleListView(ListView):
    '''
    文章列表
    '''
    model = Article
    template_name = "blog_app/article_list.html"

# #
# # class PublisherView(ListView):
# #     model = Publisher
# #     template_name = "publisher_list.html"
# #
# #     context_object_name = "publisher_list"
# #
# # class PublisherDetail(DetailView):
# #     model = Publisher
# #
# #     def get_context_data(self, **kwargs):
# #         context = super().get_context_data(**kwargs)
# #         context["book_list"] = Book.objects.all()
# #         return context
#
