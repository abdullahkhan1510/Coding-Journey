groceries = {}

while True:
    try:
        item = input("Item: ").strip().lower()
        if item in groceries:
            groceries[item] = groceries[item] + 1
        elif item not in groceries:
            groceries[item] = 1

    except EOFError:
        print("Sorted list: ")
        break
for item in sorted(groceries):
    print(groceries[item], item.upper(), sep = " --> ")