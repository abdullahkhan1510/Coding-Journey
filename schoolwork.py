import random
counts = [0, 0, 0, 0, 0, 0]
x = int(input("Seed: "))
random.seed(x)
rolls = int(input("Rolls: "))
for i in range(0,rolls):
    roll = random.randint(1,6)
    
    if roll == 1:
        counts[0] = counts[0]+1
    elif roll == 2:
        counts[1] = counts[1]+1
    elif roll == 3:
        counts[2] = counts[2]+1
    elif roll == 4:
        counts[3] = counts[3]+1
    elif roll == 5:
        counts[4] = counts[4]+1
    else:
        counts[5] = counts[5]+1
maxcount = counts[0]
for i in range(1,6):
    if counts[i] > maxcount:
        maxcount = counts[i]
        maxi = i
    else:
        pass

for i in range(len(counts)):
    num = counts[i]
    print(f"{i+1}: {num}")

print(f"Most common: {i} ({maxcount} times)")