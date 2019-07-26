# encoding: utf-8

# author    : liuzhanxiong
# email     : lzx1453536003@163.com
# IDE       : PyCharm
# time      : 2019-07-26 14:55
from django.contrib import admin
from django.contrib.admin import AdminSite
from admin_app.models import Article

class BlogAdminSite(AdminSite):
    site_header = '管理员'
    site_title = 'site admin'

    def __init__(self, name = 'admin'):
        AdminSite.__init__(self, name)

    def has_permission(self, request):
        return request.user.is_superuser


blog_admin_site = BlogAdminSite()
blog_admin_site.register(Article,admin.ModelAdmin)