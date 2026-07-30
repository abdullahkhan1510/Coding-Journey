while True:
    try:
        fraction = input("Please enter your fraction: ")
        numerator, denominator = fraction.split("/")
        numerator = int(numerator)
        denominator = int(denominator)
        if denominator == 0:
                    raise ValueError
        tank = numerator/denominator
        tank = tank * 100 
        tank = round(tank)
        if numerator > denominator:
            raise ValueError
        else:
            if tank <= 1:
                print("E")
                break
            elif tank >= 99:
                print("F")
                break
            else:
                print(tank, "%", sep = "")
                break
    except ValueError:
        print("Invalid fraction")