from django.urls import path,include
from django.contrib.auth import views as v
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('register/', views.signup_view, name="register"),
    path('',include("django.contrib.auth.urls")),
    path('login/',v.LoginView,name="login"),
    path('logout/',v.LogoutView, name = "logout"),
]
