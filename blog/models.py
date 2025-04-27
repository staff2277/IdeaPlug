from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=250)
    bg_image = models.ImageField(upload_to="media/", blank=True, null=True)
    main_content = models.TextField()
