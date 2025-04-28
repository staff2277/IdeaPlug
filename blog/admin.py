from django.contrib import admin

from blog.models import BlogPost, Employee

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Employee)
