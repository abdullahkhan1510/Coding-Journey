months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
while True:
    try:
        date = input("Date:")
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            print(f"{year}-{month:02d}-{day:02d}")
        elif "," in date:
            month, day, year = date.split(" ")
            month = month.title()
            day = int(day.replace(",", ""))
            year = int(year)
            month = months.index(month) + 1
            print(f"{year}-{month:02d}-{day:02d}")
    except ValueError:
        pass