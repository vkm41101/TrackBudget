from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from pickle import dumps, loads
import time


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    Username = None
    walletTransac = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    dob = models.DateField("Date of Birth")
    MobileNumber = models.CharField(max_length=10, unique=True, primary_key=True)
    password = models.CharField(max_length=20)
    USERNAME_FIELD = 'MobileNumber'
    REQUIRED_FIELDS = ['name', 'dob', 'password']
    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser

    @property
    def is_admin(self):
        return self.admin

    @is_staff.setter
    def is_staff(self, value):
        self.staff = value

    @is_superuser.setter
    def is_superuser(self, value):
        self.superuser = value

    @is_admin.setter
    def is_admin(self, value):
        self.admin = value

    def __str__(self):
        return "{}".format(self.MobileNumber)


class Friendship(models.Model):
    friendshipId = models.CharField(max_length=200)
    MobileNumber1 = models.CharField(max_length=10)
    MobileNumber2 = models.CharField(max_length=10)


class Transaction(models.Model):
    transactionId = models.CharField(max_length=200)
    transactionFrom = models.CharField(max_length=10)
    transactionTo = models.CharField(max_length=10)
    transactionAmount = models.IntegerField(default=0)


class pendingTransaction(models.Model):
    pendingTransactionId = models.CharField(max_length=200)
    transactionFrom = models.CharField(max_length=10)
    transactionTo = models.CharField(max_length=10)
    transactionAmount = models.IntegerField(default=0)
