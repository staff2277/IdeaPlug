from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=250)
    bg_image = models.ImageField(upload_to= 'media/', blank=True, null=True)
    main_content = models.TextField()

    
    