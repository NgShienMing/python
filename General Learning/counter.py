#!/usr/bin/env python3
"""Counter"""

def total(*num, initial = 5, **key):
    """Counter"""
    count = initial
    for number in num:
        count += number
    for k in key:
        count += key[k]
    return count

print(total(100, 2, 3, clouds = 50, stars = 100))
print(__name__)
