cart = []

k = map(str.strip, input("Enter product names to add to cart: ").split(" "))
cart.extend(k)

k = input("Enter product name to remove from cart: ")
if k in cart:
    cart.remove(k)
else:
    print("Product not found in cart.")

z = cart.pop()
print("Removed from cart:", z)

cart.sort()
print("Sorted Cart:", cart)

d = {}
for i in range(len(cart)):
    if i not in d:
        d[i+1] = cart[i]
print("Cart:", d)