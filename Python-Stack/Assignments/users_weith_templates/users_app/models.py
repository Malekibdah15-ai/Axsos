from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=45)
    Email = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    