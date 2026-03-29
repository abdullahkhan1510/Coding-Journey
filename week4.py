# Simple Temp Converter
unit = input("Is this Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the degrees: "))

if unit == "C" or unit == "c":
    new_temp = (temp * 9/5) + 32
    print("In Fahrenheit that is:", new_temp)
elif unit == "F" or unit == "f":
    new_temp = (temp - 32) * 5/9
    print("In Celsius that is:", new_temp)
else:
    print("I don't know that unit")