from django.urls import path
from . import views

app_name = "tracker" 

# including urls patterns and their rout to views 
urlpatterns = [
    path("signup/",views.signup,name="signup"),
    path("login/",views.log_in,name="login"),
    path("logout/",views.log_out,name="logout"),
    path("index/",views.index,name="index"),
    path("add/",views.add,name="add"),


]
