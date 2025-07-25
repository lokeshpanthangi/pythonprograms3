p = ["Laptop","keyboard","mouse","monitor"]
prices = [1000, 50, 20, 300]
q = [5, 10, 15, 8]



#1 Create a List of Products
z = zip(p,prices)
z2 = zip(prices, q)

#2 Calculate Total Value of Each Product
for i, j in z2:
    s = i * j
    print("Total Value of", p[prices.index(i)], ":", s)
print("DATA")


#3 Create a Dictionary from Zipped Lists
d = {}

for i in p:
    d[i] = {"price": prices[p.index(i)], "quantity": q[p.index(i)]}
print("Inventory Dictionary:", d)

#4Find Low Stock Products

for i in d:
    if d[i]["quantity"] < 10:
        print("Low Stock Product:", i, "with quantity:", d[i]["quantity"])
