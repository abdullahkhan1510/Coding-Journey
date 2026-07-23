age = int(input("Please enter a number: "))
def is_adult(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"
print(is_adult(age))