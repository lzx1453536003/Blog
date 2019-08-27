# encoding: utf-8

# author    : liuzhanxiong
# email     : lzx1453536003@163.com
# IDE       : PyCharm
# time      : 2019-08-26 17:37

from django.core import cache
from blog_app.models import get_category_tree

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
        'HEAD_TITLE' : '重剑无锋 大巧不工',
        'SITE_NAME'  : "站点名称",

        'category_tree' : get_category_tree(),
        'print_log' : print_log,
    }
    # cache.set(key, value, 60 * 60 * 10)
    return value