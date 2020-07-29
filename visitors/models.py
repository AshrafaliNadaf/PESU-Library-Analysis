from django.db import models
from user.models import Department
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.


class Visitor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    students = models.PositiveIntegerField(default=0)
    staff = models.PositiveIntegerField(default=0)
    visitors = models.PositiveIntegerField(default=0)
