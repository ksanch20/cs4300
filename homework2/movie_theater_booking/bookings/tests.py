from django.test import TestCase 
from bookings.models import Movie, Seat, Booking
from django.contrib.auth.models import User

class TestModels(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create a test movie
        self.movie = Movie.objects.create(
            title="Test Movie",
            release_date="2025-09-27",
            description="A test movie",
            duration=120
        )

        # Create seats for the movie
        self.seat1 = Seat.objects.create(seat_number="A1", movie=self.movie)
        self.seat2 = Seat.objects.create(seat_number="A2", movie=self.movie)

    def test_movie_creation(self):
        self.assertEqual(str(self.movie), "Test Movie")
        self.assertEqual(self.movie.duration, 120)

    def test_seat_creation(self):
        self.assertEqual(str(self.seat1), "Seat A1 - Available")
        self.assertFalse(self.seat1.booking_status)

