"""Week 1 Worksheet"""
# Activity 2
import math
def pythagoras(coord1: tuple, coord2: tuple):
    """Calculate the hypotenuse with Pythagoras theorem"""
    x_1 = coord1[0]
    x_2 = coord2[0]
    y_1 = coord1[1]
    y_2 = coord2[1]
    length_a = x_2 - x_1
    length_b = y_2 - y_1
    length_c = math.sqrt(length_a**2 + length_b**2)
    return f"Hypotenuse = {round(length_c, 4)} units"

coord_1 = (1, 3)
coord_2 = (4, 8)
print(pythagoras(coord_1, coord_2))

# Exercise 1
def sphere_vsa(diameter):
    """Calculate the volume and surface area of a sphere"""
    radius = diameter/2
    volume = 4/3*math.pi*radius**3
    surface_area = 4*math.pi*radius**2
    return f"Sphere with a diameter of {diameter}m has a volume of {round(volume, 2)}m3\
             and a surface area of {round(surface_area, 2)}m2"

SPHERE_DIAMETER = 13.5
print(sphere_vsa(SPHERE_DIAMETER))

# Exercise 2
def cone_vol(diameter, height):
    """Calculate the volume of a cone"""
    radius = diameter/2
    volume = 1/3*math.pi*radius**2*height
    return f"Cone with a diameter of {diameter}m and a height of {height}m\
             has a volume of {round(volume, 2)}m3"

CONE_DIAMETER = 10.25
CONE_HEIGHT = 20.5
print(cone_vol(CONE_DIAMETER, CONE_HEIGHT))

# Exercise 3
REFERENCE_STRING = "abcdefghijklmnopqrstuvwxyz"
WORD = (REFERENCE_STRING[5] + REFERENCE_STRING[14] + REFERENCE_STRING[23]).capitalize()
print(WORD)
