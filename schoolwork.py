numbers = [3, 7, 11, 15, 19, 23, 27, 31, 35]
target = 23

def binarySearch(numbers,target):
    right = len(numbers)-1
    left = 0
    while left<=right:
        mid = (right+left) // 2
        if numbers[mid] > target:
            right = mid-1
        elif numbers[mid] < target:
            left = mid+1
        elif numbers[mid] == target:
            return mid
    return -1
print("Starting binary search...")
print("Result:", binarySearch(numbers, target))
print("Program finished!")