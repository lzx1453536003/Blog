# encoding: utf-8

# author    : liuzhanxiong
# email     : lzx1453536003@163.com
# IDE       : PyCharm
# time      : 2019-08-26 17:37

from django.core import cache
from blog_app.models import get_category_tree, Article

print("logaaa")
def print_log():
    print("log")

def seo_processor(request):
    '''

    :param request:
    :return:
    '''
    key = 'seo_processor'
    # value = cache.get(key)
    # if value:
    #     return value
    # else:
    value = {
        'print_log': print_log,

        'HEAD_TITLE' : '重剑无锋 大巧不工',
        'HOME_PAGE'  : '首页',

        'category_tree' : get_category_tree(), #类别树
        'article_all' : Article.objects.all(),
    }
    # cache.set(key, value, 60 * 60 * 10)
    return value