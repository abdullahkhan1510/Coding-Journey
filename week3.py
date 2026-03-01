while True:
    try:
        x = int(input("What is your number?"))
        print("X is: ", x)
    except ValueError:
        print("X is not an integer")
    else:
        break
print("X is ", x)