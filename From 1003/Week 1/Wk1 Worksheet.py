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

coord1 = (1, 3)
coord2 = (4, 8)
print(pythagoras(coord1, coord2))

# Exercise 1
def sphere_vsa(diameter):
    radius = diameter/2
    volume = 4/3*math.pi*radius**3
    surface_area = 4*math.pi*radius**2
    return "Sphere with a diameter of {}m has a volume of {}m3 and a surface area of {}m2" .format(diameter, round(volume, 2), round(surface_area, 2))

sphereDiameter = 13.5
print(sphere_vsa(sphereDiameter))

# Exercise 2
def cone_vol(diameter, height):
    radius = diameter/2
    volume = 1/3*math.pi*radius**2*height
    return "Cone with a diameter of {}m and a height of {}m has a volume of {}m3" .format(diameter, height, round(volume, 2))

cone_diameter = 10.25
cone_height = 20.5
print(cone_vol(cone_diameter, cone_height))

# Exercise 3
reference_string = "abcdefghijklmnopqrstuvwxyz"
word = (reference_string[5] + reference_string[14] + reference_string[23]).capitalize()
print(word)