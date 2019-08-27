from django.db import models
from django.urls import reverse

class Category(models.Model):
    """
    文章类别
    """
    name = models.CharField('name', max_length=30)
    parent_category = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return ""#reverse("")

def get_category_tree(category = None):
    category_tree = {}
    categorys = Category.objects.all()
    sub_categorys = categorys.filter(parent_category=category)
    for category in sub_categorys:
        category_tree[category] = {}
    for key, value in category_tree.items():
        category_tree[key] = get_category_tree(key)
    return category_tree


# def get_category_tree():
#     category_tree = {'root':[]}
#     categorys = Category.objects.all()
#     for category in categorys:
#         if category.parent_category:
#             if category_tree[category.parent_category]:
#                 category_tree[category.parent_category].append(category)
#             else:
#                 category_tree[category.parent_category] = [category]
#         else:
#             category_tree['root'].append(category)
#     return category_tree
#
# def pre_traversal(key):
#     tree = get_category_tree()
#     node_list = tree[key]
#     if node_list:
#         for node