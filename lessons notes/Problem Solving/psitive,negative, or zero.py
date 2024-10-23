"""
year is a leap year if:
It is divisible by 4, but not divisible by 100, unless it is also divisible by 400.

if it is dividable by 4 but not 100 and not 400 -> is leap year
if it is dividable by 4 but not 100 and dividable by 400 -> not leap year

if it is dividable by 4 but and 100 and not 400 -> not leap year
if it is dividable by 4 but and 100 and not 400 -> not leap year

"""

year = int(input("please enter the year: "))

if year%4 == 0:
    if year % 400 == 0:
        if year %100 != 0:
            print("is not leap year")
        else:
            print("is leap year")
    else:
        if year %100 != 0:
            print("is leap year")
        else:
            print("is not a leap year")
else:
    print("is not a leap year")
    