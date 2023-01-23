from django import forms
from .models import Booking


class BookingForm(forms.Modelform):
    class Meta:
        model = Booking
        fields = ['name', 'guests', 'date', 'phone', 'email']