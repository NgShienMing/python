"""Week 1 Workshop Quiz"""
import math
import numpy as num

NUM1 = 5
NUM2 = 10
NUM3 = 3
TOTAL = NUM1 + NUM2 + NUM3
print(f"Sum = {TOTAL}")

print(math.ceil(num.random.rand()*-25)-1)

OPPOSITE = 1.5
ADJACENT = 3.4
angleA = math.atan(OPPOSITE/ADJACENT)*180/math.pi
angleB = math.atan(ADJACENT/OPPOSITE)*180/math.pi
print(f"Angle A: {round(angleA, 2)} degrees, Angle B: {round(angleB, 2)} degrees")
