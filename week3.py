time = input("Please enter a time: ")
hours, minutes = time.split(":")
hours = int(hours)
minutes = int(minutes)
minutes = minutes / 60
timeint = hours + minutes
if timeint >= 7.0 and timeint <= 8.0:
    print("Breakfast time")
elif timeint >= 12.0 and timeint<= 13.0:
    print("Lunch time")
elif timeint >= 18.0 and timeint <= 19.0:
    print("Dinner time")
else:
    print("Not time for any meal right now. ")