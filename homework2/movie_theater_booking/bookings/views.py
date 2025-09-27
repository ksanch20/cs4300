from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from bookings.models import Movie, Seat, Booking
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer


# -------------------------
# API Views (DRF ViewSets)
# -------------------------

# MovieViewSet for CRUD operations on movies
class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

#SeatViewSet for seat availability and booking 
class SeatViewSet(viewsets.ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()

    #Return all available seats 
    @action(detail=False, methods=['get'])
    def available(self, request):
        available = Seat.objects.filter(booking_status=False)
        serializer = self.get_serializer(available, many=True)
        return Response(serializer.data)
    
    #Return all booked seats 
    @action(detail=False, methods=['get'])
    def booked(self, request):
        booked = Seat.objects.filter(booking_status=True)
        serializer = self.get_serializer(booked, many=True)
        return Response(serializer.data)



#BookingViewSet for users to book seats and view their booking history
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def create(self, request, *args, **kwargs):
        seat_id = request.data.get("seat")
        movie_id = request.data.get("movie")

        # Check seat availability
        seat = Seat.objects.get(id=seat_id)
        if seat.booking_status:
            return Response({"error": "Seat already booked!"}, status=status.HTTP_400_BAD_REQUEST)

        # Book it
        seat.booking_status = True
        seat.save()

        # Create booking with logged-in user
        booking = Booking.objects.create(movie_id=movie_id, seat=seat, user=request.user)
        serializer = self.get_serializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


#Home page 
def home(request):
    return render(request, 'bookings/home.html')

#View to display list of all movies
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

#View to handle seat booking for specific movie
@login_required
def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all().order_by('seat_number')


    if request.method == "POST":
        seat_id = request.POST.get("seat_id")
        seat = get_object_or_404(Seat, id=seat_id)

        if seat.booking_status:
            error = "This seat is already booked."
            return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats, 'error': error})

        seat.booking_status = True
        seat.save()
        Booking.objects.create(movie=movie, seat=seat, user=request.user)
        return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

#View to display the booking history 
@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.post)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'bookings/sign_up.html', {'form': form})



