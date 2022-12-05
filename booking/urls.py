from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='mainpage'), 
    path('detail/<id>', views.movie_detail), 
    path('show', views.show_select),
    path('bookedseats', views.bookedseats),
    path('mybookings', views.userbookings),
    path('checkout', views.checkout), 
    path('booked', views.booked_ok), 
]