count = 0
def count_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
n = int(input("Please enter a number: "))
for i in range(1,n+1):
    if count_even(i) == True:
        count += 1
    else:
        count = count
print(f"{count} numbers from 1 to {n} are even")
