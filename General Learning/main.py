#!/usr/bin/env python3
"""Testing to run as main"""
import people as ppl
import day

nsm = ppl.Person("Ng Shien Ming", "June 2")
nsm.to_string()

day.calc_day_in_year(2002, 6, 2)
print(__name__)
