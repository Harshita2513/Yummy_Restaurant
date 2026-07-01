from django.contrib import admin
from .models import Menu, Chefs, Cart, Order, OrderItem
# Register your models here.
admin.site.register(Menu)
admin.site.register(Chefs)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)

