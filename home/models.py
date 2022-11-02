from pyexpat import model
from django.db import models

#Create your models here.
class Speaker(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    about = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name