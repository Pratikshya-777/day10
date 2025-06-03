from django.shortcuts import render
# from django.http import HttpResponse
from z.forms import ContactForm, FeedbackForm

# Create your views here.
def feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        # process form.cleaned_data
        print(form.cleaned_data)
        form.save()
        return render(request, 'myform/thankyou.html')
    # form = ContactForm()
     # if request.method == "POST":
        # form = ContactForm(request.POST)
        # print(form)

    context = {
        "form":form
    }
    return render (request,"myform/feedback.html",context)

def index(request):
    """django form example"""
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # process form.cleaned_data
        print(form.cleaned_data)
        return render(request, 'myform/thankyou.html')
    # form = ContactForm()
     # if request.method == "POST":
        # form = ContactForm(request.POST)
        # print(form)

    context = {
        "form":form
    }
    return render (request,"myform/forms.html",context)
    # return HttpResponse("my forms are loading")
    