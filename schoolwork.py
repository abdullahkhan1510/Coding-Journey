nums = [
    [12, 5, 8],
    [3, 19, 7],
    [11, 6, 14]
]
largest = nums[0][0]
for row in range(3):
    for col in range(3):
        if nums[row][col] > largest:
            largest = nums[row][col]
            colval = col
            rowval = row
            
print(f"Largest number is: {largest}")
print(f"Row: {rowval+1}")
print(f"Col: {colval+1}")