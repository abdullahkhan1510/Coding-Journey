def main():
    number = getnum()
    meow(number)

def getnum():
    while True:
        n = int(input("What is n?"))
        if n > 0:
            return n

def meow(n):
    for i in range(n):
        print("meow")
main()