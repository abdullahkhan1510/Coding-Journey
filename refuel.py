def main():
    fraction = input("Please enter a fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    num, den = fraction.split("/")
    num = int(num)
    den = int(den)

    if den == 0:
        raise ZeroDivisionError
    if num > den or num < 0 or den < 0:
        raise ValueError
    return round((num / den) * 100)

def gauge(percent):
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"


if __name__ == "__main__":
    main()