from django.shortcuts import render
from .models import Restaurant, Table, Reservation

# Create your views here.


def get_booking_page(request):
    return render(request, 'booking/booking.html')
