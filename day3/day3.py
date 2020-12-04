#!/usr/bin/env python3
import sys

SLOPES = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]

def mapGrid():
    return [list(line.strip()) for line in sys.stdin.readlines()]

def treeCounter(grid, right, down):
    cols = len(grid[0])
    rows = len(grid)

    curr_col = 0
    curr_row = 0
    num_trees = 0
    
    char = grid[0][0]
    if char == '#':
        num_trees += 1

    while ((curr_row := curr_row + down) < rows ):
        curr_col += right
        char = grid[curr_row][(curr_col % cols)]
        if char == '#':
            num_trees += 1

    return num_trees

def main():
    grid = mapGrid()

    mult_trees = 1
    for right, left in SLOPES:
        mult_trees = mult_trees * treeCounter(grid, right, left)
    
    print(mult_trees)
    
if __name__ == "__main__":
    main()