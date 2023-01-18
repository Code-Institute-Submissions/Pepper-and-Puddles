from django.shortcuts import render
from .models import Restaurant, Table, Reservation

# Create your views here.

# Function to render initial bookings page view


def get_booking_page(request):
    return render(request, 'booking/booking.html',)


# Function to make a reservation. If successful, user is brought to confirmation page.


def make_reservation(request, table_id):
    table = Table.objects.get(pk=table_id)
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        reservation = Reservation(table=table, date=date, time=time, name=name, phone=phone, email=email)
        reservation.save()
        table.available = False
        table.save()
        return render(request, 'reservation_confirmation.html', {'reservation': reservation})
    else:
        return render(request, 'make_reservation.html', {'table': table})