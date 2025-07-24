sales_data = [
    ("Q1", [("Jan", 1000), ("Feb", 1200), ("Mar", 1100)]),
    ("Q2", [("Apr", 1300), ("May", 1250), ("Jun", 1400)]),
    ("Q3", [("Jul", 1350), ("Aug", 1450), ("Sep", 1300)])
]

# 1. Calculate Total Sales per Quarter using unpacking
print("Total sales per quarter:")
for quarter, months in sales_data:
    total = 0
    for month, sales in months:
        total += sales
    print(f"{quarter}: {total}")

# 2. Find the Month with Highest Sales
max_month = None
max_sales = 0
for quarter, months in sales_data:
    for month, sales in months:
        if sales > max_sales:
            max_sales = sales
            max_month = (month)
print(f"Month with highest sales: {max_month}")


flat_sales = []
for quarter, months in sales_data:
    for month, sales in months:
        flat_sales.append((month, sales))
print("Flat list of monthly sales:")
print(flat_sales)


print("\nDetailed monthly sales by quarter:")
for qtr, months in sales_data:
    for mon, val in months:
        print(f"Quarter: {qtr}, Month: {mon}, Sales: {val}")
