# from this import d
from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
# from traitlets import default
from staff.models import  show
from accounts.models import Account


class reservation(models.Model):
    show = models.ForeignKey(show,on_delete=models.CASCADE)
    seat_no = models.CharField(max_length=10)
    expry = models.DateTimeField()
    booked = models.BooleanField(default=False)
    user = models.ForeignKey(Account,on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.seatno

class booking(models.Model):
    booking_code = models.CharField(max_length=100)
    user = models.ForeignKey(Account,on_delete=models.DO_NOTHING)
    show = models.ForeignKey(show,on_delete=models.CASCADE)
    seat_num = models.CharField(max_length=10)
    booked_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return str(self.seat_num+" "+self.booked_date+" "+self.show)
    
