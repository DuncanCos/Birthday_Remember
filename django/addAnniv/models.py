from django.db import models

# Create your models here.
class donnee(models.Model):
    name=models.CharField(max_length=200)
    pseudo=models.CharField(max_length=200)
