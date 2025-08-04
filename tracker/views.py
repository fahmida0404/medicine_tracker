from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    if request.method=="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        User.objects.create_user(username=username, email=email, password=password)
        return HttpResponseRedirect(reverse("tracker:login"))
    return render(request, "tracker\signup.html")

def log_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse("Hello! This is medicine tracker.")
        else:
            error_msg = {"error" :  "Incorrect credentials! Try Again."}
            return render(request, "tracker\login.html",error_msg)
        
    return render(request, "tracker\login.html")