students = ["Alice", "Bob", "Carol", "David", "Eve"]
scores = [85, 92, 78, 88, 95]

# Create a Numbered List of Students
for number, name in enumerate(students, start=1):
    print(f"{number}. {name}")

# Pair Students with Their Scores Using enumerate()
for index, name in enumerate(students):
    print(f"{name} scored {scores[index]}")

# Find Positions of High Scorers
high_scorer_positions = []
for index, score in enumerate(scores):
    if score > 90:
        high_scorer_positions.append(index)
print("Positions of students who scored above 90:", high_scorer_positions)

# Map Positions to Student Names
position_to_name = {index: name for index, name in enumerate(students)}
print("Position to Student Name Mapping:", position_to_name)