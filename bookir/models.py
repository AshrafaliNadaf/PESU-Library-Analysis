from django.db import models
from user.models import Department
from register.models import User
# Create your models here.


class Bookir(models.Model):
    deptname = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    bookissue = models.PositiveIntegerField(default=0)
    bookreturn = models.PositiveIntegerField(default=0)
    bookrenew = models.PositiveIntegerField(default=0)
