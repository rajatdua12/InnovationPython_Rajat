from django.shortcuts import render
from django.http import HttpResponse
from .forms import Contact_form


def index(request):
    return HttpResponse("Hello World!")

def about(request):
    return HttpResponse("This is my first django project.")

def welcome(request):
    return render(request, "generic.html")

def login(request):
    form = Contact_form(request.POST or None)
    if form.is_valid():
        form.save()
        form = Contact_form()
    context = {'form':form}
    return render(request, "generic.html", context)