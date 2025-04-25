from django.db import models

# Create your models here.
class MyBlog(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=250)
    