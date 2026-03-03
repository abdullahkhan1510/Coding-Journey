while True:
    try:
        score = int(input("Enter your test score: "))
        if score < 0:
            print("Score cannot be negative.")
        else:
            print("Your score is:", score)
            break
    except ValueError:
        print("That is not a valid integer.")

print("Final score entered:", score)