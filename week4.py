n = int(input("Please enter your number: "))
num = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse*10+digit
    n = n // 10
if num == reverse:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")