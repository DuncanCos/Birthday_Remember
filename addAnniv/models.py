from django.db import models

# Create your models here.
class donnee(models.Model):
    name=models.CharField(max_length=200)
    birthday=models.CharField(max_length=10)
