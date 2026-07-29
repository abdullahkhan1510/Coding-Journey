num = False
while num == False:
    try:
        number = int(input("Number: "))
        print(number*number)
        num = True
    except ValueError:
        print("Please enter a number. ")
