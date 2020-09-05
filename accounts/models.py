from django.db import models

# Create your models here.

class user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250,unique=True)
    username = models.CharField(max_length=50,unique=True)
