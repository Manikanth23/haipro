from turtle import back
from django.db import models


class Signup(models.Model):
     name=models.CharField(max_length=200)
     email=models.EmailField(blank=True)
     phone_number=models.IntegerField()
     photo=models.ImageField(blank=True)
     

     def __str__(self):
         return self.name