from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', views.base), 
    path('', views.index, name='index'), 
    path('movies', views.movies, name='movies'),
    path('banners', views.banners, name='banners'),
    path('shows', views.shows, name='shows'),
    path('users', views.users, name='users'),
    # path('addfilm', views.add_film, name='add movie'), 
    path('createfilm', views.FilmCreate.as_view(), name='film-create'),
    path('updatefilm/<pk>', views.FilmUpdate.as_view(), name='film-update'),
    path('deletefilm/<pk>', views.FilmDelete.as_view(), name='film-delete'),
    path('addbanner', views.BannerCreate.as_view(), name='banner-create'),
    path('editbanner/<pk>', views.BannerUpdate.as_view(), name='banner-update'),
    path('deletebanner/<pk>', views.BannerDelete.as_view(), name='banner-delete'),
    path('createshow', views.ShowCreate.as_view(), name='show-create'),
    path('updateshow/<pk>', views.ShowUpdate.as_view(), name='show-update'),
    path('deleteshow/<pk>', views.ShowDelete.as_view(), name='show-delete'),
    # path('addshow', views.add_show, name='add movie'), 
    path('bookings', views.bookings, name='bookings'), 
    path('users', views.users, name='users'), 
]