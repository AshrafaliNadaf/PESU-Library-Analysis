from django.db import models
from register.models import loginmodel
from datetime import datetime

class departments(models.Model):
    deptname=models.CharField(max_length=50)

    def __str__(self):
        return self.deptname



   
