from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=250, blank=True, null=True)
    bg_image = models.ImageField(upload_to="media/", blank=True, null=True)
    main_content = models.TextField()

    def __str__(self):
        return f"user => {self.user} || title => {self.title}"


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    age = models.IntegerField()
    sex = models.CharField(max_length=7)
    marriage_status = models.CharField(max_length=10)
    religion = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} || {self.position}"
