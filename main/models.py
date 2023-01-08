from django.db import models
from pickle import TRUE
# Create your models here.

class Signup(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)



class Signin(models.Model):
        id=models.AutoField(primary_key=True)
        username=models.CharField(max_length=255)
        password=models.CharField(max_length=255)