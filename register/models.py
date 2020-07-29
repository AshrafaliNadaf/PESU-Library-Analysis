from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class extendedUser(models.Model):
    usertype = models.CharField(max_length=50)
    contactnum = models.BigIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

