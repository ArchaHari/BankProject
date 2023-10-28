from django.db import models

# Create your models here.

class regmodel(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    image=models.FileField(upload_to='bankapp/static')
    pin=models.CharField(max_length=20)
    balance=models.IntegerField()
    acnum=models.IntegerField()

class addamountmodel(models.Model):
    uid=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)#automatically

class withdrawmodel(models.Model):
    uid=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)

class newsfeedmodel(models.Model):
    topic=models.CharField(max_length=50)
    content=models.CharField(max_length=1000)
    date=models.DateField(auto_now_add=True)
    image=models.FileField(upload_to='bankapp/static')

class wishlistmodel(models.Model):
    uid=models.IntegerField()
    newsid=models.IntegerField()
    topic=models.CharField(max_length=50)
    content=models.CharField(max_length=1000)
    date=models.DateField()



# class ministatementmodel(models.Model):
#     choice=[
#         ('deposit', 'deposit'),
#         ('withdraw', 'withdraw')
#     ]
#    choice=models.CharField(max_length=30,choices=choice)

class moneytransfermodel(models.Model):
    username=models.CharField(max_length=50)
    acnum=models.IntegerField()
    amount=models.IntegerField()