from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from bookings.models import Movie, Seat, Booking

class BookingAppTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create a test movie
        self.movie = Movie.objects.create(
            title="Princess Protection Program",
            description="Disney movie",
            release_date="2009-06-26",
            duration=90
        )
        # Create some seats for the movie
        self.seat1 = Seat.objects.create(seat_number="A1", movie=self.movie)
        self.seat2 = Seat.objects.create(seat_number="A2", movie=self.movie)

        self.client = Client()
        self.api_client = APIClient()
        self.api_client.force_authenticate(user=self.user)


    # Model Tests
    # Test movie string
    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Princess Protection Program")

    # Test seat string
    def test_seat_str_available(self):
        self.assertEqual(str(self.seat1), "Seat A1 - Available")
    
    # Test that booking a seat updates status to true 
    def test_seat_booking_status_update(self):
        booking = Booking.objects.create(user=self.user, movie=self.movie, seat=self.seat1)
        self.seat1.refresh_from_db()
        self.assertTrue(self.seat1.booking_status)

    # Test that seat can only be booked once
    def test_booking_unique_seat(self):
        Booking.objects.create(user=self.user, movie=self.movie, seat=self.seat1)
        with self.assertRaises(Exception):
            Booking.objects.create(user=self.user, movie=self.movie, seat=self.seat1)

    # Check that booking model correctly stores relationships and data when booking is created 
    def test_booking_relationships(self):
        booking = Booking.objects.create(user=self.user, movie=self.movie, seat=self.seat2)
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.movie, self.movie)
        self.assertEqual(booking.seat, self.seat2)
        self.assertIsNotNone(booking.booking_date)

    # View Tests
    # Test home view
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/home.html')

    # Test movie list view
    def test_movie_list_view(self):
        response = self.client.get(reverse('movies_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.movie.title)

    # Test booking a seat logging in 
    def test_book_seat_view_logged_in(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('book_seat', kwargs={'movie_id': self.movie.id}),
            {'seat_id': self.seat1.id}
        )
        self.assertRedirects(response, reverse('booking_history'))
        self.seat1.refresh_from_db()
        self.assertTrue(self.seat1.booking_status)

    # Test booking history view
    def test_booking_history_view(self):
        self.client.login(username='testuser', password='testpass')
        Booking.objects.create(user=self.user, movie=self.movie, seat=self.seat1)
        response = self.client.get(reverse('booking_history'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.seat1.seat_number)

    # API Tests
    # Tests that API correctly lists available seats 
    def test_api_available_seats(self):
        response = self.api_client.get('/api/seats/available/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2) 

    # Test that api can book a seat 
    def test_api_book_seat(self):
        data = {'seat': self.seat1.id, 'movie': self.movie.id}
        response = self.api_client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, 201)
        self.seat1.refresh_from_db()
        self.assertTrue(self.seat1.booking_status)
