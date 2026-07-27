amountdue = 50
print("Amount due:", amountdue)
while amountdue > 0:
    insert = int(input("Insert Coin: "))
    if insert == 25:
        amountdue = amountdue - 25
        print("Amount due:", amountdue)
    elif insert == 10:
        amountdue = amountdue - 10
        print("Amount due:", amountdue)
    elif insert == 5:
        amountdue = amountdue - 5
        print("Amount due:", amountdue)
    else:
        amountdue = amountdue
        print("Amount due:", amountdue)
        

        