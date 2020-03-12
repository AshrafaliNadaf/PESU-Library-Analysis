from django.db import models

# Create your models here.
class loginmodel(models.Model):
    usertype=models.CharField(max_length=50)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    contactnum=models.BigIntegerField()
    email=models.EmailField(max_length=400)

class visitors(models.Model):
    students=models.CharField(max_length=5)
    staff=models.CharField(max_length=5)
    visitors=models.CharField(max_length=5)