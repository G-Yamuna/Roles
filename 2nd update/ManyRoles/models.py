from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	r=[(1,'student'),(2,'teacher'),(3,'HOD'),(4,'principal'),(0,'guest')]
	age=models.IntegerField(null=True)
	phonenum=models.CharField(max_length=10)
	role=models.CharField(max_length=10,choices=r,default=0)