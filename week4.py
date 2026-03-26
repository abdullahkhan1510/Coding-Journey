while True:
    try:
        time, period = input("Enter time: ").split()
        period = period.upper()
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)

        if period == "AM":
            if hours == 12:
                hours = 0
        elif period == "PM":
            if hours != 12:
                hours += 12
        break
    except ValueError:
        print("Invalid format")
        pass
print(f"{hours:02d}:{minutes:02d}")