# Activity 2
import math
def pythagoras(coord1: tuple, coord2: tuple):
    x1 = coord1[0]
    x2 = coord2[0]
    y1 = coord1[1]
    y2 = coord2[1]
    a = x2 - x1
    b = y2 - y1
    c = math.sqrt(a**2 + b**2)
    return "Hypotenuse = {} units" .format(round(c, 4))

coord1 = (1,3)
coord2 = (4,8)
print(pythagoras(coord1, coord2))

# Exercise 1
def sphereVSA(diameter):
    radius = diameter/2
    volume = 4/3*math.pi*radius**3
    surfaceArea = 4*math.pi*radius**2
    return "Sphere with a diameter of {}m has a volume of {}m3 and a surface area of {}m2" .format(diameter, round(volume, 2), round(surfaceArea, 2))

sphereDiameter = 13.5
print(sphereVSA(sphereDiameter))

# Exercise 2
def coneVol(diameter, height):
    radius = diameter/2
    volume = 1/3*math.pi*radius**2*height
    return "Cone with a diameter of {}m and a height of {}m has a volume of {}m3" .format(diameter, height, round(volume, 2))

coneDiameter = 10.25
coneHeight = 20.5
print(coneVol(coneDiameter, coneHeight))

# Exercise 3
referenceString = "abcdefghijklmnopqrstuvwxyz"
word = (referenceString[5] + referenceString[14] + referenceString[23]).capitalize()
print(word)