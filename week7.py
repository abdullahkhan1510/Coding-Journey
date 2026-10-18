import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"([0-9]{1,2})(?::([0-9]{2}))? (AM|PM)", s)
    if match is None:
        raise ValueError("Invalid time")

    hour = int((match.group(1)))
    if hour < 1 or hour > 12:
        raise ValueError("Invalid time")
    if match.group(2) is None:
        minute = 0
    else:
        minute = int(match.group(2))
        if minute < 0 or minute > 59:
            raise ValueError("Invalid time")

    period = match.group(3)

    if period == "AM":
        if hour == 12:
            hour = 0

    elif period == "PM":
        if hour != 12:
            hour += 12
    return f"{hour:02d}"
...


if __name__ == "__main__":
    main()
