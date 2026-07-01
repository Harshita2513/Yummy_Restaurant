# Great. Since you're learning Django, let's build this **like a real restaurant website**, not just make it work. I'll explain the complete flow and we'll build it feature by feature.

# ---

# # Final Project Flow

# ```
# Home Page
#      │
#      ▼
# User Login/Register
#      │
#      ▼
# View Menu
#      │
#      ▼
# Add Item to Cart
#      │
#      ▼
# View Cart
#      │
#      ▼
# Increase/Decrease Quantity
#      │
#      ▼
# Checkout
#      │
#      ▼
# Order Created
#      │
#      ▼
# View Previous Orders
# ```

# This is exactly how Swiggy, Zomato, Domino's, etc. work.

# ---

# # Step 1 : Models

# You already have

# ```python
# Menu
# Order
# OrderItem
# ```

# I would just improve them slightly.

# ```python
# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     order_at = models.DateTimeField(auto_now_add=True)
#     total_price = models.DecimalField(max_digits=8, decimal_places=2)
#     is_paid = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Order {self.id}"
# ```

# and

# ```python
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def subtotal(self):
#         return self.menu.price * self.quantity
# ```

# ---

# # But wait...

# There is one missing model.

# Before ordering, users first add items to a **cart**.

# So we need

# ```
# Menu

# ↓

# Cart

# ↓

# Order
# ```

# ---

# # Step 2 : Create Cart Model

# ```python
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def subtotal(self):
#         return self.menu.price * self.quantity
# ```

# Now your models become

# ```
# Menu
# Cart
# Order
# OrderItem
# ```

# This is a proper design.

# ---

# # Step 3 : Register models

# ```python
# admin.site.register(Menu)
# admin.site.register(Cart)
# admin.site.register(Order)
# admin.site.register(OrderItem)
# ```

# ---

# # Step 4 : Home Page

# Display every food.

# ```
# Pizza

# ₹300

# [ Add to Cart ]
# ```

# ```
# Burger

# ₹200

# [ Add to Cart ]
# ```

# ```
# Pasta

# ₹250

# [ Add to Cart ]
# ```

# ---

# # Step 5 : URL

# ```
# path(
#     "cart/add/<int:id>/",
#     views.add_to_cart,
#     name="add_to_cart"
# )
# ```

# ---

# # Step 6 : Template

# Inside your menu loop

# ```html
# <a href="{% url 'add_to_cart' item.id %}"
# class="btn btn-danger">
# Add to Cart
# </a>
# ```

# ---

# # Step 7 : View

# When the button is clicked

# ```
# Pizza

# ↓

# User clicks

# ↓

# Add to Cart

# ↓

# Database stores

# User
# Pizza
# Quantity = 1
# ```

# View

# ```python
# def add_to_cart(request, id):

#     menu = Menu.objects.get(id=id)

#     cart_item, created = Cart.objects.get_or_create(
#         user=request.user,
#         menu=menu
#     )

#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()

#     return redirect("/")
# ```

# If Pizza already exists in the cart

# ```
# Pizza x1

# ↓

# Click again

# ↓

# Pizza x2
# ```

# instead of

# ```
# Pizza
# Pizza
# Pizza
# ```

# ---

# # Step 8 : Cart Page

# Create

# ```
# cart.html
# ```

# View

# ```python
# def cart(request):

#     items = Cart.objects.filter(user=request.user)

#     total = 0

#     for item in items:
#         total += item.subtotal()

#     return render(
#         request,
#         "cart.html",
#         {
#             "items": items,
#             "total": total
#         }
#     )
# ```

# ---

# Template

# ```
# Pizza

# ₹300

# Quantity : 2

# Subtotal : ₹600

# --------------
# Burger

# ₹150

# Quantity : 1

# Subtotal : ₹150

# --------------

# Total

# ₹750

# [ Checkout ]
# ```

# ---

# # Step 9 : Increase Quantity

# ```
# Pizza

# [-]

# 2

# [+]
# ```

# Click +

# ```
# Quantity becomes

# 3
# ```

# View

# ```python
# def increase(request, id):

#     item = Cart.objects.get(id=id)

#     item.quantity += 1

#     item.save()

#     return redirect("cart")
# ```

# ---

# # Step 10 : Decrease Quantity

# ```python
# def decrease(request, id):

#     item = Cart.objects.get(id=id)

#     if item.quantity > 1:
#         item.quantity -= 1
#         item.save()
#     else:
#         item.delete()

#     return redirect("cart")
# ```

# ---

# # Step 11 : Remove Item

# ```
# Pizza

# Quantity : 2

# [X Remove]
# ```

# View

# ```python
# def remove(request, id):

#     Cart.objects.get(id=id).delete()

#     return redirect("cart")
# ```

# ---

# # Step 12 : Checkout

# Suppose the cart contains

# ```
# Pizza

# 2

# Burger

# 1
# ```

# Click

# ```
# Checkout
# ```

# Now

# Create

# ```
# Order
# ```

# ```
# Order

# User

# Total Price

# ₹750
# ```

# Then create

# ```
# OrderItem

# Pizza

# 2
# ```

# and

# ```
# OrderItem

# Burger

# 1
# ```

# Finally

# Delete all cart items.

# ```
# Cart becomes empty.
# ```

# ---

# # Step 13 : View Orders

# ```
# My Orders
# ```

# ```
# Order #12

# ₹750

# 27 June

# View Details
# ```

# ---

# Click

# ```
# View Details
# ```

# ```
# Pizza

# 2

# ₹600

# Burger

# 1

# ₹150

# Total

# ₹750
# ```

# ---

# # Database Relationships

# ```
# User
#  │
#  ├────────────┐
#  │            │
#  ▼            ▼
# Cart        Order
#  │            │
#  │            ▼
#  │       OrderItem
#  │            │
#  └────────────┘
#        │
#        ▼
#       Menu
# ```

# ---

# ## Suggested implementation order

# Build the project in this exact sequence:

# 1. ✅ Create `Cart` model.
# 2. ✅ Show **Add to Cart** button on every menu item.
# 3. ✅ Implement `add_to_cart()` view.
# 4. ✅ Create the Cart page.
# 5. ✅ Show total price.
# 6. ✅ Add increase/decrease quantity buttons.
# 7. ✅ Add remove item functionality.
# 8. ✅ Implement checkout (create `Order` and `OrderItem`).
# 9. ✅ Create the Order History page.

# Following this order keeps the project manageable, and each feature builds naturally on the previous one. Once the cart is complete, the checkout logic becomes straightforward.
