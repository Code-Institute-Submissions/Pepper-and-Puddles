from django.db import models

# Create your models here.


class Booking(models.Model):
    party_size = models.IntegerField()
    min_party_size = models.IntegerField()
    max_party_size = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=30, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(40)
