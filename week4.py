n = int(input("Please enter a number: "))
for i in range(1,n+1):
    if i % 2 == 0 and i % 7 == 0:
        print("EvenSeven")
    elif i % 2 == 0:
        print("Even")
    elif i % 7 == 0:
        print("Seven")
    else:
        print(i)