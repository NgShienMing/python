"""Week 2 Practical"""
# Problem 2
import math
def stone_slabs_for_ground(alpha, beta, height):
    """Calculate number of stone slabs for an area of ground"""
    alpha_rad = alpha*math.pi/180
    beta_rad = beta*math.pi/180
    building_width = height/math.tan(alpha_rad)
    distance_between_buildings = height/math.tan(beta_rad)
    area = building_width*distance_between_buildings
    number_of_stone_slabs = math.ceil(area/(1*1))
    return f"{number_of_stone_slabs} stone slabs is required"

ANGLE_A = 53.13
ANGLE_B = 41
BUILDING_HEIGHT = 20
print(stone_slabs_for_ground(ANGLE_A, ANGLE_B, BUILDING_HEIGHT))

# Question 2
LOOKUP = "abcdefghijklmnopqrstuvwxyz"
input_seq = [[2, 1], [0, 2], [19, 3]]
WORD = ""

WORD += LOOKUP[input_seq[0][0]]
WORD += LOOKUP[input_seq[1][0]]
WORD += LOOKUP[input_seq[2][0]]
print(WORD.capitalize())

# Question 3
def projectile(theta, int_vel, height, grav):
    """
    Calculate the horizontal distance of a projectile
    achieving the same height at two time intervals
    """
    dist_1 = (int_vel**2*math.tan(theta) - int_vel*math.sqrt(int_vel**2*(math.tan(theta)**2)
              - (2*grav*height/(math.cos(theta)**2))))/(grav/(math.cos(theta))**2)
    dist_2 = (int_vel**2*math.tan(theta) + int_vel*math.sqrt(int_vel**2*(math.tan(theta)**2)
              - (2*grav*height/(math.cos(theta)**2))))/(grav/(math.cos(theta))**2)
    return f"x1: {round(dist_1, 2)}m\nx2: {round(dist_2, 2)}m"

ANGLE_THETA = 30*math.pi/180
U = 20
H = 4.5
G = 9.81
print(projectile(ANGLE_THETA, U, H, G))
