employees = [
    ("Alice", 50000, "Engineering"),
    ("Bob", 60000, "Marketing"),
    ("Carol", 55000, "Engineering"),
    ("David", 45000, "Sales")
]

# Sort by Salary
# Ascending order using sorted()
salary_ascending = sorted(employees, key=lambda x: x[1])
print("Salary Ascending:", salary_ascending)

# Descending order using sorted()
salary_descending = sorted(employees, key=lambda x: x[1], reverse=True)
print("Salary Descending:", salary_descending)

# Sort by Department, Then by Salary
department_then_salary = sorted(employees, key=lambda x: (x[2], x[1]))
print("Department then Salary:", department_then_salary)

# Create a Reversed List
reversed_employees = list(reversed(employees))
print("Reversed List:", reversed_employees)

# Sort by Name Length
name_length_sorted = sorted(employees, key=lambda x: len(x[0]))
print("Name Length Sorted:", name_length_sorted)

# Use sorted() vs .sort() Appropriately
# Using sorted() - creates new list
new_sorted_list = sorted(employees, key=lambda x: x[0])
print("Using sorted() - new list:", new_sorted_list)
print("Original list unchanged:", employees)

# Using .sort() - modifies original list
employees_copy = employees.copy()
employees_copy.sort(key=lambda x: x[0])
print("Using .sort() - modified list:", employees_copy)


