from django.shortcuts import render
from .models import Starters
def index(request) :

    food = Starters.objects.all()
    # return render(request, "index.html", { 'foods' : food})
    return render(request, 'index.html', { 'foods' : food})

# def login(request) :
