secret = 42
while True:
    num = int(input("Guess: "))
    if num != secret:
        print("Wrong, try again")
    else:
        print("Correct")
        break
    
