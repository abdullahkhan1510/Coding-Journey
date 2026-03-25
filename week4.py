while True:
    try:
        time = input("Time: ")
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)

        if 0 <= hours < 24 and 0 <= minutes < 60:
            print(f"{hours:02d}:{minutes:02d}")
            break
    except ValueError:
        pass