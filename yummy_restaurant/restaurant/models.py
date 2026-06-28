from django.db import models

class Starters(models.Model) :
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')