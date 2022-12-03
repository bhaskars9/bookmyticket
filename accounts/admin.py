# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SignUpForm, LoginForm
from .models import Account



admin.site.register(Account, UserAdmin)