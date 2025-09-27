from django.contrib import admin
from .models import Movie, Seat, Booking  # import models

# Register your models here.

# Register models to show them in admin
admin.site.register(Movie)
admin.site.register(Seat)
admin.site.register(Booking)
