#!/usr/bin/env python
"""The number of day of the date in the year"""

def calc_day_in_year(year, month, day):
    """Calculate the number of day of the date in the year"""
    number_of_days = int(day)
    feb = 28

    if int(year)%4 == 0:
        feb = 29
    for i in range(1, int(month)):
        if i == 2:
            number_of_days += feb
        else:
            if i <= 7:
                if not i%2 == 0:
                    number_of_days += 31
                else:
                    number_of_days += 30
            else:
                if not i%2 == 0:
                    number_of_days += 30
                else:
                    number_of_days += 31
    print(number_of_days)

YY = 2008
MM = 9
DD = 27
calc_day_in_year(YY, MM, DD)
