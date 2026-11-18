nums = [[0,0,0] for i in range(3)]
for row in range(1,4):
  for col in range(1,4):
    print(f"Enter number at position {row}, {col}: ", end = "")
    num = int(input())
    nums[row-1][col-1] = num
print("TABLE: ")
for row in range(3):
  for col in range(3):
    print(nums[row][col], end = " ")
  print("")
rtotal = [0,0,0]
ctotal = [0,0,0]
for row in range(1,4):
  for col in range(1,4):
    rtotal[row-1] = rtotal[row-1]+nums[row-1][col-1]
  print(f"Total for row {row} is: {rtotal[row-1]}")

for row in range(1,4):
  for col in range(1,4):
    ctotal[col-1] = ctotal[col-1]+nums[row-1][col-1]

for col in range(1,4):
   print(f"Total for col {col} is: {ctotal[col-1]}")
