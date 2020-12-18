#!/usr/bin/env python3
import sys
from math import sin, cos, radians, pi

def readNavigations():
    return [nav.strip() for nav in sys.stdin.readlines()]

def resultAction(instr, vertical, horizontal, angle):
    action = instr[0]
    magnitude = instr[1:]

    if action == 'N':
        vertical += magnitude

    if action == 'S':
        vertical -= magnitude

    if action == 'E':
        horizontal += magnitude

    if action == 'W':
        horizontal -= magnitude

    if action == 'L':
        angle = (angle + radians(magnitude)) % 2*pi

    if action == 'R':
        angle = (angle - radians(magnitude)) % 2*pi

    if action == 'F':
        if angle >= 0 and angle <= 180:
            vertical += magnitude * sin(angle)
        else:
            vertical -= magnitude * sin(angle)

        if angle >= pi/2 and angle <= pi*(3/2):
            horizontal -= magnitude * cos(angle)
        else:
            horizontal += magnitude * cos(angle)
        
    
    return vertical, horizontal, angle


def navigateShip(nav):
    vertical = 0 #North is positive. South is negative.
    horizontal = 0  #East is positive. West is negative.
    angle = 0

    for instr in nav:
        resultAction(instr, vertical, horizontal, angle)

def main():
    nav = readNavigations()
    navigateShip(nav)




if __name__ == "__main__":
    main()