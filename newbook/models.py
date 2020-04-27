from django.db import models
from register.models import User
from datetime import datetime
# Create your models here.


class Newbook(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   authorname = models.CharField(max_length=300)
   title = models.CharField(max_length=300)
   publisher = models.CharField(max_length=300)
   isbn = models.CharField(max_length=100)
   edition = models.PositiveIntegerField()
   price = models.PositiveIntegerField(default=0)
   copies = models.PositiveIntegerField(default=1)
   status = models.CharField(max_length=100)
   date = models.DateTimeField(default=datetime.now)

