from django.shortcuts import render
from .models import Table, Booking

# Create your views here.


# Index


def index(request):
    return render(request, 'booking/index.html',)


# Menu


def view_menu(request):
    return render(request, 'booking/menu.html')


# Function to render initial bookings page view


# Function to make a reservation. If successful, user is brought
#  to confirmation page.


def make_booking(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        booking = Booking(table=table, date=date, time=time,
                          name=name, phone=phone, email=email)
        booking.save()
        table.available = False
        table.save()
        return render(request, 'booking/booking_confirmation.html',
                      {'booking': booking})
    else:
        return render(request, 'booking/bookings.html')


# Contact


def contact_us(request):
    return render(request, 'contact.html')
