from django.db import models
from register.models import loginmodel
from datetime import datetime
# Create your models here.


class newbookmodel(models.Model):
   username = models.ForeignKey(
       loginmodel, to_field="username", default=None, on_delete=models.CASCADE)
   authorname = models.CharField(max_length=300)
   title = models.CharField(max_length=300)
   publisher = models.CharField(max_length=300)
   isbn = models.CharField(max_length=100)
   edition = models.PositiveIntegerField()
   price = models.PositiveIntegerField(default=0)
   copies = models.PositiveIntegerField(default=1)
   date = models.DateTimeField(default=datetime.now)
