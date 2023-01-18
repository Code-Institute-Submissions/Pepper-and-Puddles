from django.shortcuts import render
from .models import Booking

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
        # Get form data
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        party_size = request.POST['party_size']

    # Create a new reservation object
        reservation = Reservation(name=name, email=email, phone=phone,
                                  date=date, time=time, party_size=party_size)

    # Save the reservation to the database
        reservation.save()

    # Redirect to a confirmation page
        return redirect('booking/booking_confirmation.html')
    else:

        # Render the reservation form template
        return render(request, 'booking/bookings.html')


# Contact


def contact_us(request):
    return render(request, 'contact.html')
