from bookings.models import Movie, Seat, Booking
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework import viewsets


# Create your views here.

#MovieViewSet for CRUD operations on movies
class MovieViewSet(viewsets.ModelViewSet):
   
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


#SeatViewSet for seat availability and booking 
class SeatViewSet(viewsets.ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()


#BookingViewSet for users to book seats and view their booking history
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()



