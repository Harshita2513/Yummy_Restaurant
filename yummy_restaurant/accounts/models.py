from django.db import models

class Customer(models.Model) :
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phoneno = models.IntegerField()
    date = models.DateField()
    datetime = models.DateTimeField()
    people = models.IntegerField()
    message = models.TextField()