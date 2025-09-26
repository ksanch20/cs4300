from django.shortcuts import render
from bookings.models import Movie, Seat, Booking
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework import viewsets


# Create your views here.

#MovieViewSet for CRUD operations on movies
def MovieViewSet(viewsets.ModelViewSet){
   
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
}

#SeatViewSet for seat availability and booking 
def SeatViewSet(){
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()
}

#BookingViewSet for users to book seats and view their booking history
def BookingViewSet(){
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
}


