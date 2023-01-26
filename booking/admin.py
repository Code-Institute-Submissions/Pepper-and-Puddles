from django.contrib import admin
from .models import Booking, Table, Confirmed_Booking
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Booking)
admin.site.register(Table)


@admin.register(Confirmed_Booking)
class Confirmed_BookingAdmin(SummernoteModelAdmin):

    list_filter = ('table', 'start_time')
    