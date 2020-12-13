#!/usr/bin/env python3
import sys

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

def cardinalView(seats, row, col):
    cols = len(seats[0])
    rows = len(seats)

    num_adj = 0
    for col_index in range(col + 1, cols): # Right
        if seats[row][col_index] != ".":
            if seats[row][col_index] == "#":
                num_adj += 1
            break
    
    for col_index in range(col - 1, -1, -1): # Left
        if seats[row][col_index] != ".":
            if seats[row][col_index] == "#":
                num_adj += 1
            break

    for row_index in range(row - 1, -1, -1): # Up
        if seats[row_index][col] != ".":
            if seats[row_index][col] == "#":
                num_adj += 1
            break
    
    for row_index in range(row + 1, rows): # Down
        if seats[row_index][col] != ".":
            if seats[row_index][col] == "#":
                num_adj += 1
            break

    return num_adj

def diagonalView(seats, row, col):
    cols = len(seats[0])
    rows = len(seats)
    num_adj = 0
    
    row_index = row - 1
    col_index = col + 1

    while (row_index > -1) and (col_index < cols): # UP Right Diagonal
        if seats[row_index][col_index] != ".":
            if seats[row_index][col_index] == "#":
                num_adj += 1
            break
        
        row_index -= 1
        col_index += 1


    row_index = row - 1
    col_index = col - 1

    while (row_index > -1) and (col_index > -1): # Up Left Diagonal
        if seats[row_index][col_index] != ".":
            if seats[row_index][col_index] == "#":
                num_adj += 1
            break

        row_index -= 1
        col_index -= 1


    row_index = row + 1
    col_index = col - 1

    while (row_index < rows) and (col_index > -1): # Down Left Diagonal
        if seats[row_index][col_index] != ".":
            if seats[row_index][col_index] == "#":
                num_adj += 1
            break
        
        row_index += 1
        col_index -= 1


    row_index = row + 1
    col_index = col + 1

    while (row_index < rows) and (col_index < cols): # Down Right Diagonal
        if seats[row_index][col_index] != ".":
            if seats[row_index][col_index] == "#":
                num_adj += 1
            break
        
        row_index += 1
        col_index += 1   

    return num_adj

def ruleHelper(seats, row, col):
    if seats[row][col] == ".":
        return (False, ".")

    num_adj = 0
    num_adj += cardinalView(seats, row, col)
    num_adj += diagonalView(seats, row, col)

    if seats[row][col] == "L":
        return (True, "#") if num_adj == 0 else (False, "L")

    if seats[row][col] == "#":
        return (True, "L") if num_adj >= 5 else (False, "#")

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