a = int(input("Please enter a number: "))
b = int(input("Please enter a number: "))

def add(a,b):
    ab = a + b
    ab = str(ab)
    return "The sum is " + ab
print(add(a,b))