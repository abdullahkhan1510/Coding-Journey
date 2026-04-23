n = int(input("Please enter a number: "))
for i in range(1,n+1):
    if i % 2 == 0:
        print(i, ",Even")
    elif i % 2 != 0:
        print(i, ",Odd")