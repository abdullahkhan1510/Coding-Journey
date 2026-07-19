word = input("Please enter a word: ").lower()
count = 0
def is_vowel(letter):
    if letter in "aeiou":
        return True
    else:
        return False

for letter in word:
    if is_vowel(letter):
        count = count + 1

print("The word has", count, "vowels in it")
