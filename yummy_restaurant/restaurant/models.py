from django.db import models
from django.contrib.auth.models import User

class Chefs(models.Model) :
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='chef')


class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to="menu/")
    ingredients = models.TextField()

    def __str__(self):
        return self.title
    
class Order(models.Model) :
    # user, order_at, TOt_price
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_at = models.DateTimeField(auto_now_add=True)
    Tot_Price = models.DecimalField(max_digits=7, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model) :
    # order, menu, quantity
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self) :
        return self.menu.price * self.quantity
    
class Cart(models.Model) :
    # user, menu, quantity
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
     quantity = models.PositiveIntegerField(default=1)

     def subtotal(self) :
        return self.menu.price * self.quantity

# * ✅ User Registration/Login
# * ✅ Menu Page
# * ✅ Customer Model

# the next step is **Food Ordering**.

# ## Database Design

# Instead of storing orders inside `Customer`, create separate models.

# ```python
# # restaurant/models.py

# from django.db import models

# class Menu(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=7, decimal_places=2)
#     image = models.ImageField(upload_to="menu/")
#     description = models.TextField()

#     def __str__(self):
#         return self.name
# ```

# ---

# ### Order Model

# ```python
# from django.contrib.auth.models import User

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     ordered_at = models.DateTimeField(auto_now_add=True)
#     total_price = models.DecimalField(max_digits=8, decimal_places=2)

#     def __str__(self):
#         return f"Order {self.id}"
# ```

# ---

# ### OrderItem Model

# One order can contain many food items.

# ```python
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def subtotal(self):
#         return self.menu.price * self.quantity
# ```

# ---

# ## Flow

# ```
# User Login
#       │
#       ▼
# Menu Page
#       │
#       ▼
# Click "Add to Cart"
#       │
#       ▼
# Cart Page
#       │
#       ▼
# Increase/Decrease Quantity
#       │
#       ▼
# Checkout
#       │
#       ▼
# Order Saved
# ```

# ---

# ## Menu Page

# Each menu item should have

# ```
# Pizza
# ₹250

# [ Add to Cart ]
# ```

# or

# ```
# Burger
# ₹150

# [-] 2 [+]
# ```

# ---

# ## Cart

# Example:

# | Item   | Qty | Price |
# | ------ | --- | ----: |
# | Pizza  | 2   |  ₹500 |
# | Burger | 1   |  ₹150 |

# Total

# ```
# ₹650
# ```

# Button

# ```
# Place Order
# ```

# ---

# ## Place Order View

# When user clicks **Place Order**

# 1. Create an `Order`
# 2. Save each selected menu item as an `OrderItem`
# 3. Calculate total
# 4. Clear the cart
# 5. Show success page

# ---

# ## If you don't want a cart (simpler)

# You can make it like this:

# Menu

# ```
# Pizza

# Quantity: [2]

# [Order Now]
# ```

# When the button is clicked

# ```
# Create Order
# Create OrderItem
# Redirect to Success page
# ```

# No cart is involved.

# ---

# # My recommendation

# Since this is your **first full-stack Django project**, build it in this order:

# 1. ✅ Login/Register (Done)
# 2. ✅ Menu Display (Done)
# 3. **Add to Cart**
# 4. **Cart Page**
# 5. **Checkout**
# 6. **Order History**
# 7. **Admin Panel** (view all orders)
# 8. **Order Status** (Pending → Preparing → Delivered)

# This follows the same basic structure used by real food-ordering apps and will teach you Django models, relationships, sessions, and CRUD operations very well.
