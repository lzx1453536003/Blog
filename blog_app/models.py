# from django.db import models
#
# # # Create your models here.
# # class Publisher(models.Model):
# #     name = models.CharField(max_length = 30)
# #     address = models.CharField(max_length = 50)
# #     city = models.CharField(max_length=60)
# #     state_province = models.CharField(max_length=30)
# #     country = models.CharField(max_length=50)
# #     website = models.URLField()
# #
# #     class Meta:
# #         ordering = ["-name"]
# #
# #     def __str__(self):
# #         return self.name
# #

from django.db import models

class NavigationTag(models.Model):
    tag_name = models.CharField(max_length = 30)

