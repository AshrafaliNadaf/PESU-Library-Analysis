from django.db import models
from user.models import departments
from register.models import loginmodel
# Create your models here.


class bookirmodel(models.Model):
    deptname = models.ForeignKey(departments, on_delete=models.CASCADE)
    username = models.ForeignKey(
        loginmodel, to_field="username", default=None, on_delete=models.CASCADE)
    date = models.DateField()
    bookissue = models.PositiveIntegerField(default=0)
    bookreturn = models.PositiveIntegerField(default=0)
    bookrenew = models.PositiveIntegerField(default=0)
