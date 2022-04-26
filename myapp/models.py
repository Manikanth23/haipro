import email
from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    img=models.ImageField()
    phoneno=models.IntegerField()

    def __str__(self):
        return self.name