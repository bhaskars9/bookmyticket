from django import forms
from .models import *


# create a ModelForm
class filmForm(forms.ModelForm):

    class Meta:
        model = film
        fields = ('movie_name', 'movie_lang', 'movie_year', 'url')

    def __str__(self):
        return self.movie_name


class showForm(forms.ModelForm):

    class Meta:
        model = show
        fields = ('movie', 'start_date', 'end_date','showtime', 'price')
        labels = {
            'movie':'Select a Movie',
            'start_date':'Show Start Date',
            'end_date':'Show End Date',
            'showtime': 'Show time',
            'price': 'Ticket Price'
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'showtime':forms.TimeInput(attrs={'type': 'time'}),
            # 'movie':forms.Select(attrs={'class': "form-control"},choices=film.objects.all())
        }
    def __str__(self):
        return self.movie_name