# from this import d
from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
# from traitlets import default
from staff.models import  show
from accounts.models import Account
from datetime import datetime




class booking(models.Model):
    booking_code = models.CharField(max_length=100)
    user = models.ForeignKey(Account,on_delete=models.DO_NOTHING)
    show = models.ForeignKey(show,on_delete=models.CASCADE)
    seat_num = models.CharField(max_length=25)
    num_seats= models.PositiveSmallIntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    show_date = models.DateField(null=True)
    booked_date = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    
    def __str__(self) -> str:
        return self.seat_num+"@"+self.show_date.strftime("%m/%d/%Y")+" "+self.show.movie.movie_name
    
