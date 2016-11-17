from django.db import models

# Create your models here.

class Question(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class Choice(models.Model):
    content = models.CharField(max_length=128)
    vote = models.IntegerField(default=0)
    question = models.ForeignKey(Question)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
