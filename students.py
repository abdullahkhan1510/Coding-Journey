import csv

students = []
with open("names.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "house": row["home"]})
def get_name(student):
    return student["name"]

for student in sorted(students, key = get_name):
    print(f"{student['name']} is in {student['house']}")