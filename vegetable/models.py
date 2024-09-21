from django.db import models

# Create your models here.

class Receipe(models.Model):
    rec_name = models.CharField(max_length=100)
    rec_desc = models.TextField()
    rec_images = models.ImageField(upload_to="receipes")