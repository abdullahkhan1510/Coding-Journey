def binarySearch(arr, left, right, key):
    ## right = len(arr) - 1, returns right most index
    ## left = 0 as the first index in the array is 0
    ## key is the value we are looking for
    ## arr is the sorted array containing the numbers
    while left <= right: ## keep searching while there is a valid section of the list to search
        mid = (left+right) // 2 ## take the value at the middle index of the array
        if arr[mid] == key: ## if key is found return index at which it is found
            return mid
        elif arr[mid] < key: ## if the key value is greater than the value in the array at index[mid]
            left = mid+1 ##, remove the left half of the code which is the lower numbers, so now array consists of elements from index mid + 1 to right
        else:## if key not == arr[mid] or not arr[mid] < key.
            right = mid-1 ## removes greater half of list as key is < arr[mid]
    return -1 ## return to mr rahmans function which will print did not find item

def value():
  
  result = binarySearch([-1,1,2,4,7,8,10],0,6,9)
  if result == -1:
    return "Did not find key"
  else:
    return "Key found at", result


print(value())