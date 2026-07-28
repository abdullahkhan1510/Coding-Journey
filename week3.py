message = input("Please enter your message: ").lower()
for letter in message:
    if letter == "a":
        letter = letter.replace("a","")
        print(letter, end = "")
    elif letter == "e":
            letter = letter.replace("e","")
            print(letter, end = "")
    elif letter == "i":
            letter = letter.replace("i","")
            print(letter, end = "")
    elif letter == "o":
            letter = letter.replace("o","")
            print(letter, end = "")
    elif letter == "u":
            letter = letter.replace("u","")
            print(letter, end = "")
    else:
        print(letter, end = "")