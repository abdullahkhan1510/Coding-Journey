import random
def aa():
    numbers = [None] * 6
    for i in range(len(numbers)):
        numbers[i] = random.randint(1,20)
    target = random.randint(1,20)
    return numbers,target

def linearSearch(numbers,target):
    for i in range(len(numbers)):
        if target == numbers[i]:
            return f"Target found at index {i}"
        elif i == (len(numbers)-1):
            return "Target not found"
        else:
            pass

numbers,target = aa()
print(linearSearch(numbers,target))
