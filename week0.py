def main():
    time = input("What is the time? You must answer in the 24h format. ")
    converted_time = convert(time)
    if 7.0 <= converted_time <= 8.00:
        print("breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")
    else:
        print("")
def convert(time):
    minutes = int(0)
    hours, minutes = time.split(":")
    newh = int(hours)
    newm = float(minutes)
    minutes_dec = float(newm / 60)
    time = float(newh + minutes_dec)
    return time



if __name__ == "__main__":
    main()
