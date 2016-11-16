from django.db import models

# Create your models here.

class imagebook(models.Model):
    image = models.CharField(max_length=255,default='')
    creator = models.CharField(max_length=32,default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
