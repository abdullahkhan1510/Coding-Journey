try:
    x = int(input("What is your number?"))
    print("X is: ", x)
except ValueError:
    print("X is not an integer")
else:
    print("X is: ", x)