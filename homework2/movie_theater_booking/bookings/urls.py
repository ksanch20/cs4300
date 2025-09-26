from django.urls import path, include 
from bookings import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename = 'movie')
router.register(r'seats', views.SeatViewSet, basename = 'seat')
router.register(r'bookings', views.BookingViewSet, basename = 'booking')

urlpatterns = [
    path('', include(router.urls)),
]