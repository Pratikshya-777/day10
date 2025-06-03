from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "page_title": "django day3",
        "message": "welcome to day3"
    }
    return render(request,'homepage/home.html', context)

def about(request):
    context = {
        # "page_title": "django day3",
        # "message": "welcome to day3about"
    }
    return render(request,'homepage/about.html', context)

def skill(request):
    context = {
        #"page_title": "django day3",
        # "message": "welcome to day3"
    }
    return render(request,'homepage/skill.html', context)
def contact(request):
    context = {
        
       # "message": "skill page!"
    }
    return render(request, 'homepage/contact.html', context)

