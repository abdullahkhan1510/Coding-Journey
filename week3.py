age = int(input("Please enter your age: "))
def can_vote(age):
    if age >= 18 and age < 120:
        print("Can vote")
    else:
        print("Can't vote")
print(can_vote(age))