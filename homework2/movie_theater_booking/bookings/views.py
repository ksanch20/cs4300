from bookings.models import Movie, Seat, Booking
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404


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

#Home page 
def home(request):
    return render(request, 'bookings/home.html')

#View to display list of all movies
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

#View to handle seat booking for specific movie
def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    return render(request, 'bookings/seat_booking.html', {'movie': movie})

#View to display the booking history 
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})


