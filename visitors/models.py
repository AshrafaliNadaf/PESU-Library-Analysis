from django.db import models
from user.models import departments
from register.models import loginmodel
# Create your models here.


class visitorsmodel(models.Model):
    username = models.ForeignKey(
        loginmodel, to_field="username", default=None, on_delete=models.CASCADE)
    date = models.DateField()
    students = models.PositiveIntegerField(default=0)
    staff = models.PositiveIntegerField(default=0)
    visitors = models.PositiveIntegerField(default=0)
