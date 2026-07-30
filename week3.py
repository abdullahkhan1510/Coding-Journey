menu = {
    "Baja Taco": 4.25,
    "Burrito" : 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
while True:
    try:
        total = 0
        item = input("Please enter what item you want: ").lower().title()
        if item in menu:
            total = total + menu[item]
            print(f"Total: ${total:.2f}")
        else:
            pass
    except EOFError:
        break