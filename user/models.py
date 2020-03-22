from django.db import models

# Create your models here.
class loginmodel(models.Model):
    usertype=models.CharField(max_length=50)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    contactnum=models.BigIntegerField()
    email=models.EmailField(max_length=400)

class visitorsmodel(models.Model):
    students=models.CharField(max_length=5)
    staff=models.CharField(max_length=5)
    visitors=models.CharField(max_length=5)
    usertype = models.ForeignKey(loginmodel,default=None,on_delete=models.CASCADE)

class departments(models.Model):
    deptname=models.CharField(max_length=50)
    usertype = models.ForeignKey(loginmodel, default=None,on_delete=models.CASCADE)

class bookirmodel(models.Model):
    deptname=models.ForeignKey(departments,on_delete=models.CASCADE)
    usertype = models.ForeignKey(loginmodel, default=None,on_delete=models.CASCADE)
    date=models.DateField()
    bookissue=models.IntegerField()
    bookreturn=models.IntegerField()
    bookrenew=models.IntegerField()

class newbookmodel(models.Model):
   usertype = models.ForeignKey(loginmodel, default=None, on_delete=models.CASCADE)
   authorname=models.CharField(max_length=300)
   title=models.CharField(max_length=300)
   publisher = models.CharField(max_length=300)
   isbn = models.CharField(max_length=100)
   edition = models.IntegerField()
   price = models.IntegerField()
   copies = models.IntegerField()
