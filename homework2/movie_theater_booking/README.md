# Repository layout:
movie_theater_booking/
├── db.sqlite3
├── manage.py
├── Procfile
├── requirements.txt
├── README.md
├── movie_theater_booking/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── bookings/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── api_urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
└── templates/
    ├── base.html
    └── registration/



## Movie Theater Booking
A Django web application for booking movie tickets online. Users can browse available movies, view seat layouts, and securely book seats with account integration
Access deployed app here: https://movie-theater-bookinggunicorn-movie.onrender.com/ 

## Features
User authentication (sign up, login, logout)

Movie listings with descriptions

Interactive seat selection per movie

Prevents double booking of seats

Booking history per user

CSRF-protected forms

Deployed on Render


## Setup 

Clone the repository:

    git clone git@github.com:ksanch20/cs4300.git
    cd homework2

Create and activate a virtual environment:

    python3 -m venv myenv -- system - site - packages
    source myenv / bin / activate
    pip install django djangorestframework


Install dependencies:

    pip install -r requirements.txt

Run migrations:

    cd movie_theater_booking
    python manage.py migrate

Run development server:

    python manage.py runserver


## Render Deployment 

Create New Web Service Named: movie-theater-booking

Set Root Directory: homework2/movie_theater_booking

Build Command:

    pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate

Start Command:

    gunicorn movie_theater_booking.wsgi


Create Environment Variable: DJANGO_SECRET_KEY 

## AI Usage
Used chatGPT to:
- Generate basic HTML templates
- Help set up user profiles 
- Provide guidance on Django setup and configurations for deployment
- Suggest README structure and content

All AI-generated content was reviewed, modified, and integrated by developer
to ensure correctness and project-specific relevance. 




