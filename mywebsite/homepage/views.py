# # Create your views here.
# from django.shortcuts import render 
# from django.http import HttpResponse

# def index(request):
    
#     template_name ='hompage/home.html'
#     return render(request,template_name)
#     #return HttpResponse("This is my home")
    
def about(request):
    return HttpResponse("This is my about")


from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        "page_title": "Django Day 2",
        "message": "Welcome to Day 2 of Django!"
    }
    return render(request, 'hompage/home.html', context)
def greet(request , name):
    
    return render(request, 'hompage/greet.html',{'name':name})
def profile(request):
    context = {
        "name": "sabina",
        "email": "sabina7@gmail.com",
        "hobbies": ["coding","reading"]
    }
    return render(request, 'hompage/profile.html',context)