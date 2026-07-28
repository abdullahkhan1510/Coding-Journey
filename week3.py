count = 0
pin = 1234
while count < 3:
    newpin = int(input("Enter pin: "))
    if newpin == pin:
        print("Access granted")
        break
    else:
        print("Incorrect pin")
        count = count + 1
        if count == 3: 
            print("Card blocked")
            break
