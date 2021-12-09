import numpy as num
import math

num1 = 5
num2 = 10
num3 = 3
sum = num1 + num2 + num3
print("Sum = {}" .format(sum))

print(math.ceil(num.random.rand()*-25)-1)

opposite = 1.5
adjacent = 3.4
angleA = math.atan(opposite/adjacent)*180/math.pi
angleB = math.atan(adjacent/opposite)*180/math.pi
print("Angle A: {} degrees, Angle B: {} degrees" .format(round(angleA, 2), round(angleB, 2)))