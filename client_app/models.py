from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    username=models.CharField(max_length=50,unique=True,default="")
    email=models.EmailField(max_length=100,unique=True,default="")
    password=models.CharField(max_length=50,default="")
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']
    def __str__(self):
        return self.username
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.is_staff
    @property
    def is_admin(self):
        return self.is_admin
    @property
    def is_superuser(self):
        return self.is_superuser
    @property
    def is_active(self):
        return self.is_active
    class Meta:
        abstract=True
class Address(models.Model):
    houseNumber=models.PositiveIntegerField()
    street=models.CharField(max_length=100, default="")
    city=models.CharField(max_length=100,default="")
    country=models.CharField(max_length=100,default="")
    zipCode=models.PositiveIntegerField()
class Client(User):
    cin=models.CharField(max_length=8,primary_key=True, default="")
    name=models.CharField(max_length=100,default="")
    familyName=models.CharField(max_length=100,default="")
    phoneNumber=models.PositiveIntegerField(default=20000000)
    address=models.OneToOneField(Address,on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        ordering=['name','familyName']
        db_table='clients'
    def __str__(self):
        return self.name+" "+self.familyName

class Account(models.Model):
    accountNumber=models.CharField(max_length=10,primary_key=True)
    balance=models.FloatField()
    type=models.CharField(max_length=20,choices=[('saving','saving account'),('current','current'),('joint','joint')],default='current')
    #relationship between Client and Account (1-*)
    client=models.ForeignKey(Client,on_delete=models.CASCADE,null=True,blank=True)

class Operation(models.Model):
    operationNumber=models.CharField(max_length=10,primary_key=True)
    type=models.CharField(max_length=20,choices=[('deposit','deposit'),('withdraw','withdraw'),('transfer','transfer')],default='deposit')
    amount=models.FloatField()
    date=models.DateTimeField(default=datetime.datetime.now)
    #relationship between Account and Operation (1-*)
    account=models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True)