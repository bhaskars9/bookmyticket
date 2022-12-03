from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import formset_factory,modelformset_factory
from staff.models import *
from datetime import date,time
from accounts.views import is_user, user_login_required
from django.contrib.auth.decorators import (user_passes_test)
from .models import *

# Create your views here.
def index(request):
    message = """
                Welcome to movie ticket booking system
            """
    return HttpResponse(message)

def home(request):
    context = {}
    movies = film.objects.filter().values_list('id','movie_name','url', named=True)
    context = {
    'films': movies
    }
    return render(request,"index.html", context)

# def login(request):
#     if (request.method == "POST"):
#         email = request.POST.get('email')
#         passw = request.POST.get('pass')

#     return render(request,"user_login.html")

# def signup(request):

#     if (request.method == "POST"):
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         age = request.POST.get('age')
#         email = request.POST.get('fname')
#         passw = request.POST.get('pass')

#     return render(request,"user_signup.html")

def movie_detail(request,id):
    context = {}
    context["film"] = film.objects.get(id = id) 
    times = show.objects.filter(movie=id,end_date__gte=date.today()).all().values_list('id','showtime',named=True)
    # times = show.objects.filter(movie=id,end_date__gte=date.today(),start_date__lte=date.today()).all().values_list('id','showtime')
    context['showtimes'] = times
    return render(request,"movie_detail.html",context)

@user_passes_test(user_login_required, login_url='/accounts/usersignin')
def show_select(request):
    context = {}
    if(request.method == "GET" and len(request.GET)!=0):
        
        date = request.GET['date']
        # On a give date get all the shows running
        # films = film.objects.filter(show__end_date__gte=date, show__start_date__lte=date).values_list('id','movie_name','url',named=True)
        films = ""
        # add showitme >= current time + 5 min
        shows = show.objects.filter(end_date__gte=date, start_date__lte=date).select_related('movie_id','movie__url','movie__movie_name').order_by('movie_id','showtime').values_list('id','price','showtime','movie','movie__url','movie__movie_name',named=True)
        # films = film.objects.filter(end_date__gte=date).values_list('id','movie_name','url','showtime1','showtime2','showtime3', named=True)
        res_dict = {}
        
        for s in shows:
            # fields needed showid 0, price 1, showtime 2, movieid 3, movieurl 4, moviename 5,
            print(type(s),s[0])
            if(s[5] not in res_dict.keys()): #movie doesn't exit in dict
                res_dict[s[5]]={'url':s[4],'price':s[1], 'showtimes':{s[0]:s[2]}, 'movieid':s[3]}
            else: #movie already exists
                res_dict[s[5]]['showtimes'][s[0]]=s[2]
            
            
            #print(s['movie_name'], s['movie_url'], s['price'], s['id'])
            pass
        
        context = {'films':res_dict,'date':date,'shows':shows}
    
    return render(request,"show_selection.html",context)

def bookedseats(request):
    if request.method == 'GET':
           show_id = request.GET['show_id']
           show_date = request.GET['show_date']
        #    bookedseats = {}
           seats = booking.objects.filter(show=show_id,booked_date=show_date).values('seat_num')
           booked = ""
           for s in seats:
            booked+=s['seat_num']+","
            # print(s['seat_num'])

            pass

           return HttpResponse(booked[:-1])
    else:
           return HttpResponse("Request method is not a GET")

def checkout(request):
    context = {}
    if (request.method == "POST"):
        show_date = request.POST['showdate']
        seats = request.POST['seats']
        show_id = request.POST['showid']

        # user = Account.objects.get(id=request.user.id)
        showinfo = show.objects.get(id=show_id)

        booking.objects.create(booking_code="Random",user=request.user,show=showinfo,booked_date=show_date, seat_num=seats)        

        context["film"] = film.objects.get(movie_name = showinfo.movie) 
        context['sdate']=show_date
        context['seats']=seats
        context['show'] = showinfo

    return render(request,"checkout.html",context)

def booked_ok(request):
    context = {}
    return render(request,"booking_ok.html",context)

