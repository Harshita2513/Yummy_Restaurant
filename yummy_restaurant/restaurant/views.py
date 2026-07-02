from django.shortcuts import render, redirect
from .models import Menu, Chefs, Cart, Order, OrderItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
@login_required(login_url='login/')
def add_to_cart(request, id) :
    menu = Menu.objects.get(id=id)
    cart_item, created = Cart.objects.get_or_create(
        user = request.user,
        menu = menu
    )
    if not created:
        cart_item.quantity +=1
        cart_item.save()
    return redirect("/")

def cart(request) :
    item = Cart.objects.filter(user = request.user)
    total = 0
    for items in item :
        total = total + items.subtotal()
        quantity = items.quantity
    return render(request, 'cart.html', {
            'items' : item,
            'total' : total,
            'quantity' : quantity,
        })

def remove(request, id):
    Cart.objects.get(id=id).delete()
    return redirect("cart")
