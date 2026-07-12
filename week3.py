num = int(input("Please enter your even or odd number: "))
def is_even(n):
    if n % 2 == 0:
        return "Number is even"
    else:
        return "Number is odd"
print(is_even(num))