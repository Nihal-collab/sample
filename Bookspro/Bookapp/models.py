from django.db import models

class Books(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    content=models.TextField()
