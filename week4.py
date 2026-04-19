count = 0
num = int(input("Please enter a number: "))
while num > 0:
    num = num // 10
    count = count + 1

print("The length is: ", count)