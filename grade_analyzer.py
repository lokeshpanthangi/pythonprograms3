g = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

#Slice grades from index 2 to 7
a = g[2:7]
print(f"Grades from index 2 to 7: {a}")

#Use list comprehension to find grades above 85
g_85 = [x for x in g if x > 85]
print(f"Grades above 85: {g_85}")

#Replace the grade at index 3 with 95
g[3] = 95
print(f"After replacing grade at index 3 with 95: {g}")

#Append three new grades
g.append(93)
g.append(86)
g.append(88)
print(f"After appending three new grades: {g}")

#Sort in descending order and display the top 5 grades
g.sort(reverse=True)
b = g[:5]
print(f"Top 5 grades in descending order: {b}")
