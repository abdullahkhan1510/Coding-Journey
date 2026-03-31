def format_name(name):
    return name.title()

name = input("Name: ")
formatted = format_name(name)
print("Hello,", formatted)