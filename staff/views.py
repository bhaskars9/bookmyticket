# Create your views here.
from accounts.models import Account
from accounts.views import is_user, staff_required
from django.contrib import messages
from django.contrib.auth.decorators import (login_required,
                                            permission_required,
                                            user_passes_test)
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.template.context_processors import csrf

from .forms import filmForm, showForm
from .models import film, show


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

# @login_required(login_url='/accounts/adminlogin')
# @user_passes_test(staff_required, login_url='/accounts/adminlogin')
def index(request):
    context = {}
    return render(request,"dashboard.html",context)

# def login(request):
#     context = {}
#     return render(request,"admin_login.html",context)


######################################## MOVIE VIEWS
@user_passes_test(staff_required, login_url='/accounts/adminlogin')
def movies(request):
    context = {}
    
    # form = filmForm(request.POST or None, request.FILES or None)
    # if form.is_valid():
    #     form.save()
    # context['form']= form
    movies = film.objects.filter().values_list('id','movie_name','date_added', named=True)
    context = {
    'film_list': movies
    }
    return render(request,"movies.html",context)

@user_passes_test(staff_required, login_url='/accounts/adminlogin')
def add_film(request):
    if request.method == "POST":
        film_form = filmForm(request.POST, request.FILES)
        if film_form.is_valid():
            film_form.save()
        else:
            messages.error(request, 'Error saving form')
        # return redirect("webadmin:homepage")
        return HttpResponseRedirect("/admin/movies")
    film_form = filmForm()
    movies = film.objects.all()
    return render(request=request, template_name="add_film.html", context={'movie_form':film_form, 'movies':movies})
    
############################################## SHOW VIEWS

@user_passes_test(staff_required, login_url='/accounts/adminlogin')
def shows(request):
    context = {}
    # movies = film.objects.filter(deleted=False).values_list('id','movie_name','date_added', named=True)
    # context = {
    # 'films': movies
    # }
    shows = show.objects.all()
    return render(request,"shows.html",context={'shows':shows})

@user_passes_test(staff_required, login_url='/accounts/adminlogin')
def add_show(request):
    if request.method == "POST":
        show_form = showForm(request.POST, request.FILES)
        if show_form.is_valid():
            show_form.save()
        else:
            messages.error(request, 'Error saving form')
        # return redirect("webadmin:homepage")
        return HttpResponseRedirect("/admin/shows")
    show_form = showForm()
    shows = show.objects.all()
    return render(request=request, template_name="add_show.html", context={'show_form':show_form, 'shows':shows})

@user_passes_test(staff_required, login_url='/accounts/adminlogin')
def bookings(request):
    context = {}
    return render(request,"bookings.html",context)

@user_passes_test(staff_required, login_url='/accounts/adminlogin')
def users(request):
    context = {}
    users=Account.objects.filter(is_staff=False).all();
    return render(request,"users.html",context={'users':users})
