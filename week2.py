students = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russel Terrier"},
    {"name":"Drako", "house":"Slytherin", "patronus": None}
]
for i in students:
    print(i["name"],i["house"], i["patronus"], sep = ", ")