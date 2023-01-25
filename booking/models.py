from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator


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


class Table(model.Model):
    table_id = models.IntegerField()
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)

# Function to mark open table as booked, 
# or return that it is already booked otherwise.

    def reserve(self):
        if self.available:
            self.available = False
            self.save()
            return True
        else:
            return False
