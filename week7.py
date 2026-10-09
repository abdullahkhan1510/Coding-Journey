import re

name = input("What's your name?").strip()
matches = re.search(r"^(.+), (.+)$",name)
if matches:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(name)