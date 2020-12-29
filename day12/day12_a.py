#!/usr/bin/env python3
import sys
from math import sin, cos, radians, pi, degrees

def readNavigations():
    return [nav.strip() for nav in sys.stdin.readlines()]

def resultAction(instr, vertical, horizontal, angle):
    action = instr[0]
    magnitude = int(instr[1:])

    if action == 'N':
        vertical += magnitude

    if action == 'S':
        vertical -= magnitude

    if action == 'E':
        horizontal += magnitude

    if action == 'W':
        horizontal -= magnitude

    if action == 'L':
        angle = (angle + magnitude) % (360)

    if action == 'R':
        angle = (angle - magnitude) % (360)

    if action == 'F':
        vertical += magnitude * sin(radians(angle))
        horizontal += magnitude * cos(radians(angle))
        
    return vertical, horizontal, angle


def navigateShip(nav):
    vertical = 0 #North is positive. South is negative.
    horizontal = 0  #East is positive. West is negative.
    angle = 0

    for instr in nav:
        vertical, horizontal, angle = resultAction(instr, vertical, horizontal, angle)
    
    print(horizontal, vertical)
    manhattan_dist = abs(horizontal) + abs(vertical)
    return round(manhattan_dist, 3)


def main():
    nav = readNavigations()
    manhattan_dist = navigateShip(nav)
    print(manhattan_dist)




if __name__ == "__main__":
    main()