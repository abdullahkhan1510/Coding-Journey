students = ["Hermione", "Harry", "Zulay", "Ron"]

print("Checking the attendance list...")

for student in students:
    if student == "Zulay":
        print("Found", student.lower(), ", he is the leader today.")
    else:
        print(student, " is present.")