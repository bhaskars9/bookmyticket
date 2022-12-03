from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.base), 
    path('index', views.index, name='index'), 
    path('movies', views.movies, name='movies'),
    path('shows', views.shows, name='Shows'),
    path('addfilm', views.add_film, name='add movie'), 
    path('addshow', views.add_show, name='add movie'), 
    path('bookings', views.bookings, name='bookings'), 
    path('users', views.users, name='users'), 
]