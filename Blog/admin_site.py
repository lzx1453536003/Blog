# encoding: utf-8

# author    : liuzhanxiong
# email     : lzx1453536003@163.com
# IDE       : PyCharm
# time      : 2019-08-24 16:56

from django.contrib.admin import AdminSite
from blog_app.models import Category

class BlogAdminSite(AdminSite):
    site_header = 'DjangoBlog administration'
    site_title = 'DjangoBlog site admin'

    def __init__(self, name='admin'):
        super().__init__(name)

    def has_permission(self, request):
        return request.user.is_superuser

admin_site = BlogAdminSite(name = 'site')

admin_site.register(Category)