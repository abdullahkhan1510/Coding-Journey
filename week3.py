name = input("Please enter your name: ")
def greet(n):
    n = n.strip().title()
    return "Hello " + n + "!"
print(greet(name))