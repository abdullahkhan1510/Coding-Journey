while True:
    shape = input("Enter shape to draw: ").lower()   
    if shape == "triangle":
        break
    elif shape == "square":
        break
    else:
        print("Invalid input. Try again.")
        pass
while True: 
    desc = input("Filled or unfilled? ").lower()
    if desc == "filled":
        break
    elif desc == "unfilled":
        break
    else: 
        print("Invalid input. Try again.")
while True:
    size = int(input("Size: "))
    if not (size >= 1 and size <= 100):
        print("Invalid input. Try again.")
    else:
        print("")
        break

symbol = "*"
for i in range(size):
    if shape == "square":
        if desc == "filled":
            print(symbol*size)
        else:
            if i == 1:
                print(symbol*size)
            elif i == size-1:
                print(symbol*size)
            else:
                print("*" + " " * (size - 2) + "*")
    else:
        if desc == "filled":
            print(symbol*(i+1))
        else:
            if i == 0:
                print("*")
            elif i == size - 1:
                print("*" * size)
            else:
              print("*" + " " * (i - 1) + "*")