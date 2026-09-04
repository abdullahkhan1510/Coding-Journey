import sys


if len(sys.argv) < 2:
    sys.exit("Too few arguments")
if len(sys.argv) > 2:
    sys.exit("Too many arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")


try:
    with open(sys.argv[1], "r") as file:
        print("a")
except FileNotFoundError:
    sys.exit("File does not exist")
