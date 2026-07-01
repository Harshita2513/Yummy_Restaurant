from django.shortcuts import render
from .models import Menu, Chefs
from django.contrib import messages
def index(request) :

    food = Menu.objects.all()
    chef = Chefs.objects.all()
    # return render(request, "index.html", { 'foods' : food})
    return render(request, 'index.html', { 'foods' : food, 'chef' : chef})

def order(request) :
    if request.method == "POST":
        food = Menu.objects.all()
        messages.info(request,'Order Added')
        return render(request, 'index.html')
    else :
        return render(request, 'index.html')
