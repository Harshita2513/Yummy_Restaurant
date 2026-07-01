from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# class Customer(models.Model) :
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phoneno = models.CharField(max_length=15)
#     date = models.DateField()
#     time = models.TimeField()
#     people = models.IntegerField()
#     message = models.TextField()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=15)
    date = models.DateField(default=timezone.now)
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField()

class helpCustomer(models.Model) :
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject= models.TextField()
    message = models.TextField()