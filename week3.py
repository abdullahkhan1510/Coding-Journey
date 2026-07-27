entered = input("camelCase:")
enteredlen = len(entered)
print("Snakecase:", end = "")
for letter in entered:
    if letter.isupper():
        print("_", end = "")
        letter = letter.lower()
        print(letter, end = "")
    else:
        print(letter, end = "")