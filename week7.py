import re
email = input("What's your email?").strip()

if re.search(r"^\w+@\w+\.(edu$ | gov | net | icloud)", email):
    print("Valid")
else:
    print("Invalid")