#!/usr/bin/env python3
import sys
from math import sin, cos, radians, pi, degrees

compass = {0:(1,0), 90: (0,1), 180: (-1,0), 270: (0,-1)}

def readNavigations():
    return [nav.strip() for nav in sys.stdin.readlines()]

def rotateWay(angle, vertical, horizontal): 
    new_vertical = vertical * cos(angle) + horizontal * sin(angle)
    new_horizontal = horizontal * cos(angle) - vertical * sin(angle)
    
    return new_vertical, new_horizontal

def resultAction(action, magnitude, vertical, horizontal):
    if action == 'N':
        vertical += magnitude

    if action == 'S':
        vertical -= magnitude

    if action == 'E':
        horizontal += magnitude

    if action == 'W':
        horizontal -= magnitude

    if action == 'L':
        angle = radians(magnitude % 360)
        vertical, horizontal = rotateWay(angle, vertical, horizontal)

    if action == 'R':
        angle = radians( (-magnitude) % 360)
        vertical, horizontal = rotateWay(angle, vertical, horizontal)
        
    return vertical, horizontal


def navigateShip(nav):
    ship_vertical = 0
    ship_horizontal = 0

    way_vertical = 1 #North is positive. South is negative.
    way_horizontal = 10  #East is positive. West is negative.

    for instr in nav:
        action = instr[0]
        magnitude = int(instr[1:])

        if action == "F":
            ship_vertical += magnitude * way_vertical
            ship_horizontal += magnitude * way_horizontal
            # print(f"Ship: {ship_horizontal} {ship_vertical}")
        else:
            way_vertical, way_horizontal = resultAction(action, magnitude, way_vertical, way_horizontal)
            # print(f"Waypoint: {way_horizontal} {way_vertical}")
    
    manhattan_dist = abs(ship_vertical) + abs(ship_horizontal)
    return round(manhattan_dist)

def main():
    nav = readNavigations()
    manhattan_dist = navigateShip(nav)
    print(manhattan_dist)




if __name__ == "__main__":
    main()