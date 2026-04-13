age = int(input("Please enter your age:"))
if age >= 65:
    print("Senior")
elif age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")