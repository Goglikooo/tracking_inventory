from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=30)
    serial_number = models.CharField(max_length=50)
    price = models.FloatField()

