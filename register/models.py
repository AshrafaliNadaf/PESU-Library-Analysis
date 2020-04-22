from django.db import models

# Create your models here.


class loginmodel(models.Model):
    usertype = models.CharField(max_length=50)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    contactnum = models.BigIntegerField()
    email = models.EmailField(max_length=400)

    def __str__(self):
        return self.username
