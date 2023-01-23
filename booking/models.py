from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Booking(models.Model):
    date = models.DateField()
    guests = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(16)],
                                         null=True)
    name = models.CharField(max_length=30, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    email = models.EmailField()
# Make bookings objects list by name variable

    def __str__(self):
        return self.name
