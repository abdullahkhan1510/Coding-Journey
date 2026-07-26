card = input("Please enter your credit card number: ")
cardlen = len(card)
cardlen = int(cardlen)
ogdig = 4
stars = cardlen-ogdig

for i in range(cardlen):
    if cardlen - i > 4:
        print("*", end = "")
    else:
        print(card[i], end = "")