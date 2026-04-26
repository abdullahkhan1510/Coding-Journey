count = 0
n = int(input("Please enter a number:"))
for i in range(1,n+1):
    if i % 3 == 0 or i % 5 == 0:
        count += 1
print("The count is," ,count)