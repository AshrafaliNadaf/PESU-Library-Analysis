from django.db import models
from register.models import User
from datetime import datetime
# Create your models here.


class Newbook(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   authorname = models.CharField(max_length=300)
   title = models.CharField(max_length=300)
   publisher = models.CharField(max_length=300)
   isbn = models.CharField(max_length=100, default=0)
   edition = models.PositiveIntegerField()
   price = models.PositiveIntegerField(default=0)
   copies = models.PositiveIntegerField(default=1)
   status = models.CharField(max_length=100)
   ack = models.PositiveIntegerField(default=0)
   date = models.DateTimeField(default=datetime.now)
   role = models.CharField(max_length=100)
   usn = models.CharField(max_length=100)

