from django.db import models
# from accounts.models import Account
# from django.forms import *

class film(models.Model):
    movie_name = models.CharField(max_length = 100)
    movie_lang = models.CharField(blank=True, null=True,max_length = 100)
    movie_year = models.IntegerField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
#     active = models.BooleanField(default=True)
#     date_added = models.DateField(auto_now=False, auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.movie_name

class show(models.Model):
    movie = models.ForeignKey(film,on_delete=models.CASCADE,blank=True,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    price = models.PositiveIntegerField()
    showtime = models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    # modifiedby = models.OneToOneField(Account,on_delete=models.SET_NULL)


    def __str__(self):
        return self.showtime
