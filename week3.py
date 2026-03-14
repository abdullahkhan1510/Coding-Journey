months = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
]

while True:
    try:
        date = input("Date: ")

        # Slash format: 9/8/1636
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            # Validate and print
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break

        # Comma format: September 8, 1636
        elif "," in date:
            month_name, day, year = date.split(" ")
            day = int(day.replace(",", ""))
            year = int(year)
            month = months.index(month_name) + 1  # Convert month name to number

            # Validate and print
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break

    except:
        # Invalid input → loop continues
        pass