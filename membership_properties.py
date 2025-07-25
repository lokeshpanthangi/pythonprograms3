fruits_list = ["apple", "banana", "orange", "apple", "grape"]
fruits_tuple = ("apple", "banana", "orange")
fruits_set = {"apple", "banana", "orange", "grape"}
fruits_dict = {"apple": 5, "banana": 3, "orange": 8, "grape": 2}

k = [fruits_list, fruits_tuple, fruits_set, fruits_dict]

for i in k:
    if "apple" in i:
        print("Found 'apple' in:" , k.index(i))




print("Length of each collection:")
for i in k:
    print("length of :" , k.index(i), "is", len(i))


for i in k:
    print("Elements in collection", k.index(i), ":", end=" ")
    print()
    for z in i:
        print("Element:", z)
    print()


#4 Compare Membership Testing Performance

# Membership testing performance varies across data structures:
# - Lists: O(n) time complexity, as it requires scanning through each element.
# - Tuples: Similar to lists, O(n) time complexity, but generally faster due to immutability.
# - Sets: O(1) average time complexity, as it uses a hash table for quick lookups.
# - Dictionaries: O(1) average time complexity for key lookups, as it also uses a hash table.


#5 Demonstrate Different Iteration Patterns

for i in k[0]:
    print("Element:", i)
for i in k[1]:
    print("Element:", i)
for i in k[2]:
    print("Element:", i)
for i in k[3]:
    print("Key:", i, "Value:", k[3][i])