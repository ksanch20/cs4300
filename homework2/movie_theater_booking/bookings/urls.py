from django.urls import path, include
from . import views

urlpatterns = [
    #Home page
    path('', views.home, name='home'),

    #Movie list page showing available movies
    path('movies/', views.movie_list, name='movies-list'),

    #Seat booking page for specific movie
    path('book-seat/<int:movie_id>/', views.book_seat, name='book_seat'),

    #Booking history page 
    path('bookings/', views.booking_history, name='bookings-list'),

    path('accounts/', include('django.contrib.auth.urls')),


]
