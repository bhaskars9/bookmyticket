from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import  Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
# Create your views here.


def staff_required(user):
    return user.is_authenticated and  user.is_staff

def user_login_required(user):
    return user.is_authenticated

def is_user(user):
    return not user.is_staff

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('/accounts/usersignin')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'user_register.html', {'form': form, 'msg': msg})


def user_login(request):
    if request.user.is_authenticated:
        # return render(request, 'account_index.html')
        return redirect('/')
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:
            # if user is not None and user.role==1:
                login(request, user)
                return redirect('/admin')
            # elif user is not None and user.is_customer:
            elif user is not None and not user.is_staff:
            # elif user is not None and user.role==0:
                login(request, user)
                return redirect('/')
            # elif user is not None and user.is_employee:
            #     login(request, user)
            #     return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'

    return render(request, 'user_signin.html', {'form': form, 'msg': msg})

def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        # return render(request, 'account_index.html')
        return redirect('/admin')
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:
            # if user is not None and user.role==1:
                login(request, user)
                return redirect('/admin')
            # elif user is not None and user.is_customer:
            elif user is not None and not user.is_staff:
            # elif user is not None and user.role==0:
                login(request, user)
                return redirect('/')
            # elif user is not None and user.is_employee:
            #     login(request, user)
            #     return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'

    return render(request, 'admin_login.html', {'form': form, 'msg': msg})
    # return render(request,)

@user_passes_test(staff_required, login_url='/adminlogin')
def admin(request):
    return render(request,'admin.html')

@login_required(login_url='/login')
def customer(request):
    return render(request,'customer.html')


def signout(request):
    if request.user.is_staff:
        url = "/admin"
    else:
        url = "/"
    logout(request)
    return redirect(url)
 