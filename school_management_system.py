school = {
    "Math": {
        "teacher": "Mr. Smith",
        "students": [("Alice", 85), ("Bob", 92), ("Carol", 78)]
    },
    "Science": {
        "teacher": "Ms. Johnson",
        "students": [("David", 88), ("Eve", 94), ("Frank", 82)]
    }
}

score = 0
for k in school:
    print(f"teaches are {school[k]['teacher']}")

for i in school:
    for j in range(len(school[i]["students"])):
        score += school[i]["students"][j][1]
print("Total Average:", score/6)

# Find Top Student Across All Classes
top_student = (None, 0)  # Initialize with no student and grade 0

for subject, details in school.items():
    for name, grade in details["students"]:  # Use tuple unpacking
        if grade > top_student[1]:
            top_student = (name, grade)

print("Top Student Across All Classes:", top_student[0], "with grade", top_student[1])

