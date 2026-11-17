nums = [[0,0,0] for i in range(3)]
for row in range(1,4):
    for col in range(1,4):
        print("Enter a number for the position ",row,", ",col,": ", sep = "",end = "")
        num = int(input())
        nums[row-1][col-1] = num
print("Table:")
ctotal = [0,0,0]
rtotal = [0,0,0]
for row in range(0,3):
    for col in range(0,3):
        print(nums[row][col], end = " ")
        rtotal[row] = rtotal[row] + nums[row][col]
        ctotal[col] = ctotal[col] + nums[row][col]
    print("")
print(ctotal)
print(rtotal)