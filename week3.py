months = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}
while True:
    try:
        date = input("Please enter a date: ")
        if "/" in date:
            month, day, year = date.split("/")
            if int(month) > 12:
                raise ValueError
            if int(day) > 31:
                raise ValueError
            if int(day) < 10:
                day = day.zfill(2)
            if int(month) < 10:
                month = month.zfill(2)
            print(year, month, day, sep="-")
            break
        elif "," in date:
            date = date.strip().title()
            date = date.replace(",", "")
            month, day, year = date.split(" ")
            if month not in months:
                raise ValueError
            if int(day) > 31:
                raise ValueError
            newmonth = str(months[month])
            if int(day) < 10:
                day = day.zfill(2)
            if int(newmonth) < 10:
                newmonth = newmonth.zfill(2)
            print(year, newmonth, day, sep="-")
            break
    except (ValueError, KeyError):
        pass