reverse = ""

word = input("Please enter a word: ")

for letter in word:
    reverse = letter + reverse

print("The reversed word is:", reverse)