def GetName(name):
    for i in range(len(Contact)):
        count = 0
        current = Contact[i]
        for letter in current:
            if letter == ":":
                break
            else:
                count = count + 1
        currentName = current[0:count]
        currentEmail = current[count+1:]
        if currentName == name:
            return currentEmail
        else:
            pass
    print(current, count)