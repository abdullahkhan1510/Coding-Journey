nums = [
    [14, 7, 3],
    [8, 21, 5],
    [12, 9, 16]
]
target = int(input("Enter target number: "))
def linearSearch(nums,target):
    for row in range(3):
        for col in range(3):
                if nums[row][col] == target:
                    colval = col
                    rowval = row
                    return(f"Target found at position {rowval+1}, {colval+1}")

print(linearSearch(nums,target))