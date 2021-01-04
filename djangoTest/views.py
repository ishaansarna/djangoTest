from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request, name="World"):
    return render(request, "djangoTest/index.html", {
        "name": name.capitalize()
    })
