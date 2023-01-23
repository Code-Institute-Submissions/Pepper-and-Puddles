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
        form = BookingForm(request.POST)
        if form_is_valid():
            form.save()
            return redirect('booking/')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
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
    return render(request, 'booking/contact.html')


def show_bookings(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/show_bookings.html', context)
