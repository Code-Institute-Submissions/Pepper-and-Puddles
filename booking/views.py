from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Booking, Confirmed_Booking
from .forms import BookingForm, ConfirmedBookingsForm, AddTable

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
            return redirect('Confirmed_Booking')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'booking/bookings.html', context)


def confirmed_booking(request):
    if request.method == 'POST':
        form = ConfirmedBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Confirmed_Booking')
    form = ConfirmedBookingForm()
    context = {
        'form': form
    }
    return render(request, 'booking/confirmed_booking.html', context)


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('Confirmed_Booking')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'booking/edit_booking.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('Confirmed_Booking')

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


def add_table(request):
    if request.method == 'POST':
        form = AddTable(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_table_management')
    form = AddTable()
    context = {
        'form': form
    }
    return render(request, 'booking/admin_table_management.html', context)


def edit_table(request, table_id):
    booking = get_object_or_404(Table, id=table_id)
    if request.method == 'POST':
        form = AddTable(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect('Admin_Table_Management')
    form = AddTable(instance=table)
    context = {
        'form': form
    }
    return render(request, 'booking/admin_table_management.html', context)


def delete_table(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('Confirmed_Booking')
