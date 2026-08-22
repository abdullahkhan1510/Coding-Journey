def main():
    text = input("Input:")
    print(value(text))

def value(greeting):
    if greeting == "hello":
        return 0
    elif greeting == "hello there":
        return 0
    elif greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100





if __name__ == "__main__":
    main()