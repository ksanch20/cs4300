from django.urls import path, include 
from bookings import views 
from rest_framework.routers import DefaultRouter

#Create a DefaultRouter for automatic URL routing of Viewsets 
router = DefaultRouter()

#Register each ViewSet with the roughter 
router.register(r'movies', views.MovieViewSet, basename = 'movie')
router.register(r'seats', views.SeatViewSet, basename = 'seat')
router.register(r'bookings', views.BookingViewSet, basename = 'booking')

#Include all the router-generated URLs in the app's URL patterns 
urlpatterns = [
    path('', include(router.urls)),
]