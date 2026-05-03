count = 0
word = input("Please enter a word: ")

for i in word:
    if "a" in i:
        count += 1

print(f"The letter a appears in your word {count} times")
