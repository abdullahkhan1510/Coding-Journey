names = []
with open ("names.csv") as file:
    for line in sorted(file, reverse = True):
        print(f"Hello, {line.rstrip()}")
