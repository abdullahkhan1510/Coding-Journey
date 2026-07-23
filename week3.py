a = int(input("Please enter a number: "))
b = int(input("Please enter a number: "))
def compare(a, b):
    if a > b:
        return "First is larger"
    elif b > a:
        return "Second is larger"
    else:
        return "They are equal"
print(compare(a,b))