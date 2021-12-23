#!/usr/bin/env python3
"""Testing to run as main"""
import people as ppl
import day

def total(*num, initial = 5, **key):
    """Counter"""
    count = initial
    for number in num:
        count += number
    for k in key:
        count += key[k]
    return count

nsm = ppl.Person("Ng Shien Ming", "June 2")
nsm.to_string()

day.calc_day_in_year(2002, 6, 2)

print(total(100, 2, 3, clouds = 50, stars = 100))
print(__name__)
