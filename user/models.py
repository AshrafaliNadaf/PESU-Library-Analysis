from django.db import models
from register.models import extendedUser
from datetime import datetime

class Department(models.Model):
    deptname=models.CharField(max_length=50)

    def __str__(self):
        return self.deptname



   
