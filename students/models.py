from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    std = models.IntegerField()
    school = models.ForeignKey('auth.User', related_name='students', on_delete = models.CASCADE)
