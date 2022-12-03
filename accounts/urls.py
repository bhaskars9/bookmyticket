from django.urls import path
from . import views

urlpatterns = [
    path('usersignin/', views.user_login, name='user login'),
    path('userregister/', views.user_signup, name='user register'),
    path('adminlogin/', views.admin_login, name='admin login'),
    path('adminsignup/', views.admin_signup, name='admin register'),
    path('logout/', views.signout, name="logout"), 

]