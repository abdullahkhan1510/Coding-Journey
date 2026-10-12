numbers = [10,12,14,16,20,24,34,48]
target = 32

def linearSearch(target):
    for i in range(len(numbers)):
        if target == numbers[i]:
            return f"Target found at index {i}"
        elif i == (len(numbers)-1):
            return "Target not found"
        else:
            pass

print(linearSearch(target))