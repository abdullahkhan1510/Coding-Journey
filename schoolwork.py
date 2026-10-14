message = input("Message: ")
highestcount = 0
mostletter = ""
for letter in message:
    count = 0
    for character in message:
        if letter == character:
            count = count+1
    if count > highestcount:
        highestcount = count
        mostletter = letter
    value = ord(letter)
    if highestcount == count and value < ord(mostletter):
        mostletter = letter
print(f"{mostletter} {highestcount}")