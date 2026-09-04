import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
if not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")

info = []
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(",")
            info.append({
                "first": first.strip(),
                "last": last.strip(),
                "house": row["house"]
            })
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
    for row in info:
        writer.writerow(row)