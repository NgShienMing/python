#!/usr/bin/env python

def calcDayInYear():
    year = 2008 #input("Enter Year: ")
    month = 9 #input("Enter Month: ")
    day = 27 #input("Enter Day: ")
    numberOfDays = int(day)
    feb = 28

    if (int(year)%4 == 0):
        feb = 29
    for i in range(1, int(month)):
        if (i == 2):
            numberOfDays += feb
        else:
            if (i <= 7):
                if not(i%2 == 0):
                    numberOfDays += 31
                else:
                    numberOfDays += 30
            else:
                if not(i%2 == 0):
                    numberOfDays += 30
                else:
                    numberOfDays += 31
    
    print(numberOfDays)
print(__name__)