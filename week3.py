def main():
    x = get_int("What's x?")
    print("x is", x)

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()