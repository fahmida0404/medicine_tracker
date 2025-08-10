from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Creating views here.

def signup(request):
    # creating new user object in User model in database
    if request.method=="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        User.objects.create_user(username=username, email=email, password=password)
        return HttpResponseRedirect(reverse("tracker:login"))
    return render(request, "tracker\signup.html")

def log_in(request):
    # authenticating user credentials 
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, "tracker\index.html")
        else:
            error_msg = {"error" :  "Incorrect credentials! Try Again."}
            return render(request, "tracker\login.html",error_msg)
    return render(request, "tracker\login.html")

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("tracker:login"))