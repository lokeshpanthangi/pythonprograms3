inventory = {
    "apples": {"price": 1.50, "quantity": 100},
    "bananas": {"price": 0.75, "quantity": 150},
    "oranges": {"price": 2.00, "quantity": 80}
}

# Add a New Product
k = input("Enter new product name: ")
kp = float(input("Enter product price: "))
kq = int(input("Enter product quantity: "))
inventory[k] = {"price":kp, "quantity": kq}

# Update Product Price
inventory["bananas"]["price"] = 0.85

# Sell 25 Apples
inventory["apples"]["quantity"] -= 25

# Calculate Total Inventory Value
total_inventory_value = 0
for i in inventory:
    for z in i:
        total_inventory_value += inventory[i]["price"] * inventory[i]["quantity"]
print("Total Inventory Value:", total_inventory_value)

# Find Low Stock Products
low_stock_products = []
for details in inventory.values():
    if details["quantity"] < 100:
        low_stock_products.append(details)
print("Low Stock Products:", low_stock_products)
