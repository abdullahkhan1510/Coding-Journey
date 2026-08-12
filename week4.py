import random
n = 0
while n <= 0:
    n = int(input("Level: "))
value = random.randint(1,n+1)
while True:
    entered = int(input("Guess:"))
    if entered < value:
        print("Too small!")
    elif entered > value:
        print("Too large!")
    elif entered == value:
        print("Just right!")
        break
