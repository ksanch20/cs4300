from rest_framework import serializers 
from bookings.models import Movie, Seat, Booking

#Serializer for Movie model
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie 
        fields = ['title', 'description', 'release_date', 'duration']

#Serializer for Seat model
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['seat_number', 'booking_status']

#Serializer for Booking
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['movie', 'seat', 'user', 'booking_date']



