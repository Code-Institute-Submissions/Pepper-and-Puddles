from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Confirmed_Bookings
from .forms import BookingForm, ConfirmedBookingsForm

# Create your views here.


# Index


def index(request):
    return render(request, 'booking/index.html',)


# Menu


def view_menu(request):
    return render(request, 'booking/menu.html')


# Function to request a booking, before time is validated.

def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Confirmed_Bookings')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'booking/bookings.html', context)


def confirmed_bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Confirmed_Bookings')
    form = BookingConfirmedForm()
    context = {
        'form': form
    }
    return render(request, 'booking/bookings.html', context)


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('Confirmed_Bookings')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'booking/edit_booking.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('Confirmed_Bookings')

# Contact


def contact_us(request):
    return render(request, 'booking/contact.html')

# Booking log


def show_bookings(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/show_bookings.html', context)
