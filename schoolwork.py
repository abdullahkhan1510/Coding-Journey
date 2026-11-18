nums = [
    [3, 8, 2],
    [7, 1, 9],
    [4, 6, 5]
]
smallest = [0,0,0]
for col in range(3):
  smallest[col] = nums[0][col]
  for row in range(3):
    if nums[row][col] < smallest[col]:
      smallest[col] = nums[row][col]
for i in range(3):
  print(f"Smallest in column {i+1}: {smallest[i]}")
