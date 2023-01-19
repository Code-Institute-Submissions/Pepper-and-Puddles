from django.db import models

# Create your models here.


class Booking(models.Model):
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=30, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    email = models.EmailField()
