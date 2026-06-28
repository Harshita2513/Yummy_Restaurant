from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import Customer
def register(request) :
    if request.method == "POST" :
        name = request.POST['name']
        email = request.POST['email']
        phoneno = request.POST['phoneno']
        date = request.POST['date']
        datetime = request.POST['datetime']
        people = request.POST['people']
        message = request.POST['message']
 
        if User.objects.filter(email = email).exists() :
            messages.info(request, "User already exists")
            return redirect("register")


        elif User.objects.filter(phoneno= phoneno).exists() : 
            messages.info(request, "Phone no. already exists")
            return redirect("/accounts/register")

        else : 
            user = User.objects.create_user(username=name, email=email)
            Customer.objects.create(
                phoneno=phoneno, 
                date= date, 
                datetime = datetime, 
                people=people, 
                message= message
            )
            user.save()
            print("User saved successfully")
            messages.success(request, "Customer booked successfully")

            return redirect("register")


    else : 
         return render(request, "register.html")

# def login(request) :
#     if request.method == "POST" :
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username = username, password = password)

#         if user is not None : 
#             auth.login(request, user)
#             print("User Login successfully!!")
#             return redirect('/')
#         else : 
#             messages.info(request, 'False Credentials')
#             return redirect('login')

#     else :
#         # redirect('/')
#         return render(request, 'login.html')

# def logout(request) :
#     auth.logout(request)
#     return  redirect('/')