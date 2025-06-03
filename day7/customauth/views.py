from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def dashboard(request):
        return HttpResponse("you can view this response")
    
def profile(request):
    if not request.user.is_authenticated:
        return HttpResponse("you are not allowed to view")
    context = {
        "message":"you can view this"
    }
    return render(request, "customauth/profile.html",context)

# @login_required(login_url="login")
def new(request):
    if not request.user.is_authenticated:
        return HttpResponse("you canot view this")
    context = {
        "message":"you can view this"
    }
    return render(request, "customauth/new.html",context)