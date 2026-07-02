'''
There are still a few mistakes.

### 1. This line is wrong

```python
quantity = Cart.quantity
```

`Cart` is the **model class**, not a cart object. It has no class attribute called `quantity`.

Instead, each cart item has its own quantity.

For example:

```python
items = Cart.objects.filter(user=request.user)
```

Then each item has:

```python
item.quantity
```

or

```python
for item in items:
    print(item.quantity)
```

---

### 2. You don't need to send `quantity` separately

You're already sending:

```python
'items': item
```

In `cart.html`, you can simply do:

```django
{% for item in items %}
    {{ item.menu.title }}
    {{ item.quantity }}
{% endfor %}
```

No need for

```python
'quantity': quantity
```

So your `cart()` view should be:

```python
def cart(request):
    items = Cart.objects.filter(user=request.user)

    total = 0
    for item in items:
        total += item.subtotal()

    return render(request, "cart.html", {
        "items": items,
        "total": total,
    })
```

---

### 3. Your `remove()` view is incorrect

You wrote:

```python
Cart.objects.get(id=id).delete()
```

Here, `id` is probably the **Menu id** from:

```html
remove/{{ foody.id }}/
```

But `Cart.id` and `Menu.id` are different.

Instead:

```python
def remove(request, id):
    cart_item = Cart.objects.get(user=request.user, menu_id=id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect("cart")
```

This decreases the quantity first and only removes the item when the quantity becomes 0.

---

### 4. Your template condition is still wrong

You cannot do:

```django
{% if quantity > 1 %}
```

because there is no global `quantity`.

If you're displaying the cart, use:

```django
{% for item in items %}
    {{ item.menu.title }}
    {{ item.quantity }}

    {% if item.quantity > 1 %}
        ...
    {% endif %}
{% endfor %}
```

---

## One question

Do you want your home page (`index.html`) to behave like **Swiggy/Zomato**, where each food item shows:

```
Pizza

[-] 2 [+]

```

after adding it to the cart, **instead of** showing only an "Add to Cart" button?

Or do you want to keep the home page simple and manage quantities only on the cart page?

'''