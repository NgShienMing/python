# Problem 2
import math
def stone_slabs_for_ground(alpha, beta, height):
    alpha_rad = alpha*math.pi/180
    beta_rad = beta*math.pi/180
    building_width = height/math.tan(alpha_rad)
    distance_between_buildings = height/math.tan(beta_rad)
    area = building_width*distance_between_buildings
    number_of_stone_slabs = math.ceil(area/(1*1))
    return "{} stone slabs is required" .format(number_of_stone_slabs)

alpha = 53.13
beta = 41
height = 20
print(stone_slabs_for_ground(alpha, beta, height))

# Question 2
LOOKUP = "abcdefghijklmnopqrstuvwxyz"
input = [[2, 1], [0, 2], [19, 3]]
word = ""

word += LOOKUP[input[0][0]]
word += LOOKUP[input[1][0]]
word += LOOKUP[input[2][0]]
print(word.capitalize())

# Question 3
def projectile(theta, u, h, g):
    x1 = (u**2*math.tan(theta) - u*math.sqrt(u**2*(math.tan(theta)**2) 
          - (2*g*h/(math.cos(theta)**2))))/(g/(math.cos(theta))**2)
    x2 = (u**2*math.tan(theta) + u*math.sqrt(u**2*(math.tan(theta)**2) 
          - (2*g*h/(math.cos(theta)**2))))/(g/(math.cos(theta))**2)
    return "x1: {}m\nx2: {}m" .format(round(x1, 2), round(x2, 2))

theta = 30*math.pi/180
u = 20
h = 4.5
g = 9.81
print(projectile(theta, u, h, g))