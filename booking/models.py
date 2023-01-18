from django.db import models

# Create your models here.


class Table(models.Model):
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=30, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(40)
