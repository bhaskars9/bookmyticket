from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'), 
    path('users', views.users, name='users'), 
    # CRUD Film
    path('movies', views.movies, name='movies'),
    path('createfilm', views.FilmCreate.as_view(), name='film-create'),
    path('updatefilm/<pk>', views.FilmUpdate.as_view(), name='film-update'),
    path('deletefilm/<pk>', views.FilmDelete.as_view(), name='film-delete'),
    # CRUD Banner
    path('banners', views.banners, name='banners'),
    path('addbanner', views.BannerCreate.as_view(), name='banner-create'),
    path('editbanner/<pk>', views.BannerUpdate.as_view(), name='banner-update'),
    path('deletebanner/<pk>', views.BannerDelete.as_view(), name='banner-delete'),
    # CRUD Shows
    path('shows', views.shows, name='shows'),
    path('createshow', views.ShowCreate.as_view(), name='show-create'),
    path('updateshow/<pk>', views.ShowUpdate.as_view(), name='show-update'),
    path('deleteshow/<pk>', views.ShowDelete.as_view(), name='show-delete'),
]