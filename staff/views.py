# Create your views here.
from accounts.models import Account
from accounts.views import is_user, staff_required
from booking.models import booking
from django.contrib import messages
from django.contrib.auth.decorators import (login_required,
                                            permission_required,
                                            user_passes_test)
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.template.context_processors import csrf
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Avg, Count, Min, Sum
from datetime import date, timedelta
from .forms import filmForm, showForm
from .models import film, show, banner


# from .forms import filmForm, showForm
# from .models import film, show

def handler401(request, *args, **argv):
    return render(request, '401.html', status=401)

def handler404(request, *args, **argv):
    return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)


def base(request):
    return render(request,"admin_base.html")


################################################ LOGING VIEWS

@user_passes_test(staff_required, login_url='/accounts/adminlogin')
def index(request):
    context = {}
    start_date = date.today() - timedelta(days=2)

    b_data = booking.objects.filter(show_date__gte=start_date).values_list('show_date').order_by('show_date').annotate(total_seats=Sum('num_seats'))
    r_data = booking.objects.filter(show_date__gte=start_date).values_list('show_date').order_by('show_date').annotate(total=Sum('total'))
    
    booking_table = booking.objects.select_related().order_by('-booked_date').values_list('show_date','booked_date','show','total','num_seats','show__movie__movie_name','show__showtime','user__username',named=True)
    # booking_table = booking.objects.filter(booked_date__gte=start_date).select_related('user__username').order_by('booked_date').values_list('booked_date','show','total','num_seats','user__username',named=True)
    # shows = booking.objects.filter(booked_date__gte=start_date).select_related('show_id','movie__url','movie__movie_name').order_by('booked_date').values_list('booked_date','show','total','num_seats','user',named=True)

    movies_count = film.objects.all().count()
    users_count = Account.objects.filter(is_staff=False).count()
    bookings_count = booking.objects.all().count()

    days = 7
    date_labels = set(start_date + timedelta(x) for x in range(days))
    date_labels = sorted(date_labels)
    
    # res={"dates":[],"tickets":[]}
    graph1 = {}
    data_dict = {}
    for r in b_data:
        # legend of fields: date 0, no of tickets 1
        data_dict[r[0]]=r[1]
    for d in date_labels:
        if(d not in data_dict.keys()):
            data_dict[d]=0
    graph1['dates']=",".join([ x.strftime("%b %d") for x in date_labels])
    graph1['tickets']=[data_dict[x] for x in date_labels ] 

 # res={"dates":[],"tickets":[]}
    graph2 = {}
    data_dict = {}
    for r in r_data:
        # legend of fields: date 0, no of tickets 1
        data_dict[r[0]]=r[1]
    for d in date_labels:
        if(d not in data_dict.keys()):
            data_dict[d]=0
    graph2['dates']=",".join([ x.strftime("%b %d") for x in date_labels])
    graph2['total']=[data_dict[x] for x in date_labels ] 


    context={
        'graph1':graph1,
        'graph2':graph2,
        'tabledata':booking_table,
        'movies_count':movies_count,
        'users_count':users_count,
        'bookings_count':bookings_count
        }
    
    return render(request,"dashboard.html",context)

# def login(request):
#     context = {}
#     return render(request,"admin_login.html",context)

##################### FILM VIEWS #####################################

class FilmCreate(CreateView):
    template_name = "film/add_film.html";
    model = film;
    fields = ['movie_name','movie_lang','movie_genre','movie_year','url','movie_plot'];
    success_url = reverse_lazy('movies');


class FilmUpdate(UpdateView):
    template_name = "film/edit_film.html";
    model = film;
    fields = ['movie_name', 'movie_lang', 'movie_genre','movie_year','url','movie_plot'];
    success_url = reverse_lazy('movies');


class FilmDelete(DeleteView):
    template_name = "film/delete_film.html";
    model = film;
    success_url = reverse_lazy('movies');

##################### FILM VIEWS #####################################

class BannerCreate(CreateView):
    template_name = "banner/add_banner.html";
    model = banner;
    fields = ['movie', 'url'];
    success_url = reverse_lazy('banners');


class BannerUpdate(UpdateView):
    template_name = "banner/add_banner.html";
    model = banner;
    fields = ['movie', 'url'];
    success_url = reverse_lazy('banners');


class BannerDelete(DeleteView):
    template_name = "banner/delete_banner.html";
    model = banner;
    success_url = reverse_lazy('banners');

##################### SHOW VIEWS #####################################

class ShowCreate(CreateView):
    template_name = "show/add_show.html";
    form_class: showForm
    model = show;
    fields = ['movie', 'start_date', 'end_date','price','showtime'];
    success_url = reverse_lazy('shows');


class ShowUpdate(UpdateView):
    template_name = "show/edit_show.html";
    form_class: showForm
    model = show;
    fields = ['movie', 'start_date', 'end_date','price','showtime'];
    success_url = reverse_lazy('shows');


class ShowDelete(DeleteView):
    template_name = "show/delete_show.html";
    model = show;
    success_url = reverse_lazy('shows');


################# USERS
def users(request):
    users = Account.objects.filter(is_staff=False).values_list('username','email', named=True)
    return render(request,"users.html",{'users': users})


######################################## MOVIE VIEWS
@user_passes_test(staff_required, login_url='/accounts/adminlogin')
def movies(request):
    movies = film.objects.filter().order_by('-id').values_list('id','movie_name','movie_genre','date_added','movie_lang','url','movie_year', named=True)
    return render(request,"movies.html",{'film_list': movies})

######################################## MOVIE VIEWS
@user_passes_test(staff_required, login_url='/accounts/adminlogin')
def banners(request):
    banner_data = banner.objects.all().select_related().values_list('id','movie__movie_name','url','modified', named=True)
    return render(request,"banners.html",context = {'banners': banner_data})

############################################## SHOW VIEWS

@user_passes_test(staff_required, login_url='/accounts/adminlogin')
def shows(request):
    shows = show.objects.all().order_by('-id')
    return render(request,"shows.html",context={'shows':shows})

# @user_passes_test(staff_required, login_url='/accounts/adminlogin')
# def bookings(request):
#     context = {}
#     return render(request,"bookings.html",context)

# @user_passes_test(staff_required, login_url='/accounts/adminlogin')
def users(request):
    context = {}
    users=Account.objects.filter(is_staff=False).all();
    return render(request,"users.html",context={'users':users})

# # @user_passes_test(staff_required, login_url='/accounts/adminlogin')
# def add_film(request):
#     if request.method == "POST":
#         film_form = filmForm(request.POST, request.FILES)
#         if film_form.is_valid():
#             film_form.save()
#         else:
#             messages.error(request, 'Error saving form')
#         # return redirect("webadmin:homepage")
#         return HttpResponseRedirect("/admin/movies")
#     film_form = filmForm()
#     movies = film.objects.all()
#     return render(request=request, template_name="add_film.html", context={'movie_form':film_form, 'movies':movies})
   