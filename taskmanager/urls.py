"""taskmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from booking import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('bookings/', views.make_booking, name='Bookings'),
    path('confirmed_bookings/', views.confirmed_booking,
         name='ConfirmedBooking'),
    path('admin_table_management/',
         views.add_table, name='admin_table_management'),
    path('menus/', views.view_menu, name='Menus'),
    path('contact/', views.contact_us, name='Contact'),
    path('', views.index, name='Home'),
    path('show_bookings/', views.show_bookings, name='Confirmed_Booking'),
    path('edit_booking/<booking_id>', views.edit_booking, name='Edit_Booking'),
    path('delete/<booking_id>', views.delete_booking, name='delete'),
    path('edit/<table_id>', views.edit_table, name='edit_table'),
    path('delete/<table_id>', views.delete_table, name='delete_table'),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += staticfiles_urlpatterns()
