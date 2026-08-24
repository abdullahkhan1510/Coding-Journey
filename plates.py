def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    number = False
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0:2].isalpha() == False:
        return False
    for i in s:
        if not i.isalpha() and not i.isdigit():
            return False
        elif number == False and i == "0":
            return False
        elif i.isdigit():
            number = True
        elif number:
            return False
    

    return True

    


main()