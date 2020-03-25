from django.db import models

# Create your models here.
class loginmodel(models.Model):
    usertype=models.CharField(max_length=50)
    username=models.CharField(max_length=200,unique=True)
    password=models.CharField(max_length=200)
    contactnum=models.BigIntegerField()
    email=models.EmailField(max_length=400)

class visitorsmodel(models.Model):
    students=models.CharField(max_length=5)
    staff=models.CharField(max_length=5)
    visitors=models.CharField(max_length=5)
    username = models.ForeignKey(loginmodel,to_field="username",default=None,on_delete=models.CASCADE)

class departments(models.Model):
    deptname=models.CharField(max_length=50)

    def __str__(self):
        return self.deptname

class bookirmodel(models.Model):
    deptname=models.ForeignKey(departments,on_delete=models.CASCADE)
    username = models.ForeignKey(loginmodel,to_field="username", default=None,on_delete=models.CASCADE)
    date = models.DateField()
    bookissue = models.PositiveIntegerField(default=0)
    bookreturn = models.PositiveIntegerField(default=0)
    bookrenew = models.PositiveIntegerField(default=0)

class newbookmodel(models.Model):
   username = models.ForeignKey(loginmodel,to_field="username",default=None, on_delete=models.CASCADE)
   authorname=models.CharField(max_length=300)
   title=models.CharField(max_length=300)
   publisher = models.CharField(max_length=300)
   isbn = models.CharField(max_length=100)
   edition = models.PositiveIntegerField(default=0)
   price = models.PositiveIntegerField(default=0)
   copies = models.PositiveIntegerField(default=0)
   