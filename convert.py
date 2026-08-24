def main():
    number = int(input("Input: "))
    print(f"Fahrenheit: {convert(number)}")

def convert(temp):
    fah = temp * 9/5
    fah = fah + 32
    return fah

if __name__ == "__main__":
    main()