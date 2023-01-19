from django.db import models
from guest_no_validation import Valid_Guest_Amount
# Create your models here.


class Booking(models.Model, guests):
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField("Please tell us how many"
                                 " guests are in your party.")
    name = models.CharField(max_length=30, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    email = models.EmailField()
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.name
