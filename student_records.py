s = [
    (101, "Alice", 85, 20),
    (102, "Bob", 92, 19),
    (103, "Carol", 78, 21),
    (104, "David", 88, 20)
]

# 1. Find the Student with the Highest Grade
h = None
m = 0
for x in s:
    id, n, g, a = x
    if g > m:
        m = g
        h = x
print(f"Student with highest grade: {h}")

# 2. Create a Name-Grade List
ng = []
for x in s:
    id, n, g, a = x
    ng.append((n, g))
print(f"Name-Grade list: {ng}")

# 3. Demonstrate Tuple Immutability
print("\nDemonstrating tuple immutability:")
print(f"Original student record: {s[0]}")
try:
    # This will cause an error because tuples are immutable
    s[0][2] = 90  # Trying to change Alice's grade
except TypeError as e:
    print(f"Error: {e}")
    print("Tuples are immutable - you cannot change individual elements")
    print("This is why tuples are preferred for records like student data:")
    print("- Data integrity: Prevents accidental modification")
    print("- Thread safety: Multiple threads can safely access tuples")
    print("- Hashable: Tuples can be used as dictionary keys")
    print("- Memory efficient: Tuples use less memory than lists")
