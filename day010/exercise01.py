# Leap year checker using functions

# Allow to enter an year
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))


def is_leap(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

    else:
        return False


def days_in_month(year, month):
    if month > 12 and month < 1:
        return

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


days = days_in_month(year=year, month=month)
print(f"Number of days in {month} is {days}")
