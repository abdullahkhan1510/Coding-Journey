names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break
length = len(names)
if length == 1:
    print()
    print("Adieu, adieu to", name)
elif length == 2:
    print()
    print("Adieu, adieu, to", names[0], "and", names[1])
else:
    last = names.pop()
    print()
    print(last)
    print("Adieu, adieu, to", ", ".join(names) + ", and", last)