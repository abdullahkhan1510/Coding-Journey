i = 1
password = input("\n What is your password?").strip()
while i != 0:
    pass2 = input("Please reenter your original password").strip()
    if pass2 == password:
        print("You may proceed.")
        i == 0
    else:
        i = i + 1