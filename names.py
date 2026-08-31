import csv

students = []
with open("names.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "house": row[1]})

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")