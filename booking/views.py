from django.shortcuts import render

# Create your views here.


def get_booking_page(request):
    return render(request, 'booking/booking.html')
