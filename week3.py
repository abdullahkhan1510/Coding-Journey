num = int(input("Please enter a number: "))
def mot(n):
    if n % 3 == 0:
        return "True"
    else:
        return "False"
for i in range(1, num+1):
    if mot(i) == "True":
        print(i)
