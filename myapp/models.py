from django.db import models


# Create your models here.
class Viewers(models.Model):
  username=models.CharField(max_length=30)
  email=models.EmailField()
  password=models.CharField()
  subscription=models.CharField(max_length=20)

