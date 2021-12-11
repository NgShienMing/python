#!/usr/bin/env python3
"""Drawing shapes by printing *"""
import math

def draw_cross(size: int):
    """Draw a cross"""
    arr = ["*"]*size
    front = 0
    back = size - 1
    output = ""
    while not front == size and not back == -1:
        for i in range(size):
            arr[i] = " "
        arr[front] = "*"
        arr[back] = "*"
        for j in range(size):
            output += arr[j]
        output += "\n"
        front += 1
        back -= 1
    print(output)

def draw_plus(size: int):
    """Draw a plus"""
    output = ""
    for i in range(1, size+1):
        if not i == math.ceil(size/2):
            output += " "*math.floor(size/2) + "*" + " "*math.floor(size/2) + "\n"
        else:
            output += "*"*size + "\n"
    print(output)

def draw_z(size):
    """Draw a Z"""
    output = ""
    for row in range(size+1):
        for col in range(size):
            if row in (0, size):
                output += "*"
            elif (row+col) == size:
                output += "*"
            else:
                output += " "
        output += "\n"
    print(output)

def draw_rectangle(width, height):
    """Draw a rectangle"""
    output = ""
    for i in range(1, height+1):
        if i in (1, height):
            output += "*"*width + "\n"
        else:
            output += "*" + " "*(width-2) + "*" + "\n"
    print(output)

SIZE = 5
WIDTH = 5
HEIGHT = 6
draw_cross(SIZE)
draw_plus(SIZE)
draw_z(SIZE)
draw_rectangle(WIDTH, HEIGHT)
