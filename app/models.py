from django.db import models

# Create your models here.
class User(models.Model):
    profile = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

