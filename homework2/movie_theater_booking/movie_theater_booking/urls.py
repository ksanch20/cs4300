"""
URL configuration for movie_theater_booking project.

"""
from django.contrib import admin
from django.urls import path, include 



urlpatterns = [
    path('admin/', admin.site.urls), # Admin panel
    path('api/', include('bookings.api_urls')), # Include bookings app URLs under /api/
    path('', include('bookings.urls')), #Template-based URLs
]
