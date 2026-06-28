from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import Customer
def register(request) :
    if request.method == "POST" :
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        phoneno = request.POST['phoneno']
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        message = request.POST['message']

        if password == password2 :

            if User.objects.filter(username = username).exists() :
                messages.info(request, "User already exists")
                return redirect("register")


            elif User.objects.filter(email= email).exists() : 
                messages.info(request, "Email already exists")
                return redirect("register")

            else : 
                # user = User.objects.create_user(username=name, email=email)
                # Customer.objects.create(
                #     name = name,
                #     email = email,
                #     phoneno=phoneno, 
                #     date= date, 
                #     time = time, 
                #     people=people, 
                #     message= message
                # )
                # user.save()
                user = User.objects.create_user(
                username=username,
                email=email,
                password=password
                )

                Customer.objects.create(
                    user = user,
                    name=name,
                    phoneno=phoneno,
                    date=date,
                    time=time,
                    people=people,
                    message=message
                )
                # user.save()

                print("User saved successfully")
                messages.success(request, "Customer booked successfully")

                return render(request, "register.html", {'users' : user})
        else:
            messages.info(request, "Password didn't match")
            return redirect("register")

    else : 
         return render(request, "register.html")

def login(request) :
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        # if Customer.objects.filter(username = username).exists() :
        #     auth.login(request,)

        if user is not None : 
            auth.login(request, user)
            print("User Login successfully!!")
            return redirect('/')
        else : 
            messages.info(request, 'False Credentials')
            return redirect('login')

    else :
        # redirect('/')
        return render(request, 'login.html')

def logout(request) :
    auth.logout(request)
    return  redirect('/')