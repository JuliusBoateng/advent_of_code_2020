#!/usr/bin/env python3
import sys

DIRECTIONS = [
    [-1, 0],
    [1,  0],
    [0, -1],
    [0,  1],
    [-1,-1],
    [-1, 1],
    [1, -1],
    [1,  1]
]

def readSeats():
    seats = [["."] + list(line.strip()) + ["."] for line in sys.stdin.readlines()]
    padding = ["." for _ in range(len(seats[0]))]
    return [padding] + seats + [padding]

def printSeats(seats):
    rows = len(seats)
    cols = len(seats[0])

    for row in range(1, rows - 1):
        result = ""
        for col in range(1, cols - 1):
            result += seats[row][col]
        print(result)

def ruleHelper(seats, row, col):
    if seats[row][col] == ".":
        return (False, ".")

    num_adj = 0
    for x, y in DIRECTIONS:
        if seats[row + x][col + y] == "#":
            num_adj += 1
    
    if seats[row][col] == "L":
        return (True, "#") if num_adj == 0 else (False, "L")

    if seats[row][col] == "#":
        return (True, "L") if num_adj >= 4 else (False, "#")

def applyRule(seats):
    rows = len(seats)
    cols = len(seats[0])
    rule_applied = False

    new_seats = [["." for col in range(cols)] for row in range(rows)]

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            val, new_seats[row][col] = ruleHelper(seats, row, col)

            if val == True:
                rule_applied = True
    
    return rule_applied, new_seats

def repeatedRules(seats):
    val, modified_seats = applyRule(seats)

    while (val):
        val, modified_seats = applyRule(modified_seats)
    
    return modified_seats

def countOccupied(seats):
    rows = len(seats)
    cols = len(seats[0])
    count = 0

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if seats[row][col] == "#":
                count += 1

    return count

def main():
    seats = readSeats()
    modified_seats = repeatedRules(seats)
    printSeats(modified_seats)

    num_occupied = countOccupied(modified_seats)
    print(num_occupied)
    

if __name__ == "__main__":
    main()