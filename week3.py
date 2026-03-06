while True:
    try:
        fraction = input("Enter your fraction:")
        num1, num2 = fraction.split("/")
        num1 = int(num1)
        num2 = int(num2)
        if num1 > num2:
            continue
        else:
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
percent = round(num1/num2*100)
if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{percent}%")