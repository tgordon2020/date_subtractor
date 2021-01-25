import datetime


def time_sub():
    src_time = int(input("Do you want to subtract from current time(1) or specified time(2)"))
    if src_time == 1:
        #current time
        pass
    elif src_time == 2:
        print("Enter starting time")
        src_year = int(input("Enter Year: "))
        src_month = int(input("Enter Month: "))
        src_day = int(input("Enter Day: "))
        src_hour = int(input("Enter Hour: "))
        src_minute = int(input("Enter Minute: "))
    else:
        print("Please enter 1 for current time, or 2 for specified time")
        time_sub()

    print("Enter time to subtract")
    weeks = int(input("Number of Weeks: "))
    days = int(input("Number of Days: "))
    hours = int(input("Number of Hours: "))
    minutes = int(input("Number of Minutes: "))

    if src_time == 1:
        print(datetime.datetime.now() - datetime.timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes))
    else:
        print(datetime.datetime(year=src_year, month=src_month, day=src_day, hour=src_hour, minute=src_minute) - datetime.timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes))

    return

    
if __name__=="__main__":
    print("""### Datetime Subtractor.  Subtract date/time from current time or specified time
    """)
    time_sub()
