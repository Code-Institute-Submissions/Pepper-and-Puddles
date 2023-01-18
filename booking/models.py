from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(40)
