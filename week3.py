day = input("Please enter a day of the week: ").title()
def weekend(day):
    if day == "Sunday" or day == "Saturday":
        return "Weekend"
    else:
        return "Weekday"
print(weekend(day))