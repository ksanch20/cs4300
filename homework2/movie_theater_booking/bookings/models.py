from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Movie Model
class Movie(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text = "Duration in minutes")

    def __str__(self):
        return self.title
    
#Seat model
class Seat(models.Model):
    seat_number = models.CharField(max_length = 10)
    booking_status = models.BooleanField(default=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="seats")

    class Meta:
        unique_together = ('movie', 'seat_number')

    def __str__(self):
        return f"Seat {self.seat_number} - {'Booked' if self.booking_status == True else 'Available'}"

#Booking model
class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} booked {self.seat} for {self.movie}"




