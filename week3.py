a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
def is_larger(num1,num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Numbers are equal"
print(is_larger(a,b))