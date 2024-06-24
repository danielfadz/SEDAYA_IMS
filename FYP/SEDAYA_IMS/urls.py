from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="index"),
    path("homepage", views.homepage, name="homepage"),
    path('home', views.home, name='home'),
    path("loginselection", views.loginselection, name="loginselection"),
    path("booking", views.booking, name="booking"),
    path("registration", views.registration, name="registration"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("chart", views.chart, name="chart"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("adminhome", views.adminhomepage, name="adminhome"),
    path("adminbooking", views.adminbooking, name="adminbooking"),
    path("adminregistration", views.adminregistration, name="adminregistration"),
    path("adminaboutus", views.adminaboutus, name="adminaboutus"),
    path("adminchart", views.adminchart, name="adminchart"),
]
