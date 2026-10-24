import re


def main():
    print(extract(input("Text: ")))


def extract(s):
    matches = re.findall(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", s)
    return matches


if __name__ == "__main__":
    main()