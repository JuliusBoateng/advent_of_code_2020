#!/usr/bin/env python3
import sys
from collections import defaultdict
from itertools import product
import copy

def readState():
    y = 0
    z = 0

    cubeStates = defaultdict(lambda : ".")
    while line := sys.stdin.readline().strip():
        for x, char in enumerate(list(line)):
            cubeStates[(x, y, z)] = char

        y += 1
    
    return cubeStates

def conwayAlgHelper(state, deltas, cubeStates, newCubeStates):
    neighbors = []
    active_neighbors = 0
    new_neighbors = set()
    
    for delta in deltas:
        neighbor = tuple(map(lambda x,y : x + y, state, delta))
        neighbors.append(neighbor)

        if neighbor in cubeStates:
            if cubeStates[neighbor] == '#':
                active_neighbors += 1
        else:
           new_neighbors.add(neighbor)

    if cubeStates[state] == '#':
        if (active_neighbors == 2) or (active_neighbors == 3):
            newCubeStates[state] = '#'
        else:
            newCubeStates[state] = '.'
    else:
        if active_neighbors == 3:
            newCubeStates[state] = '#'
        else:
            newCubeStates[state] = '.'

    return new_neighbors

def conwayAlg(cubeStates):
    deltas = set(product([0,1,-1], repeat=3))
    deltas.remove((0,0,0))

    for i in range(6):
        newCubeStates = defaultdict(lambda : ".")
        new_neighbors = set()

        for state in cubeStates:
            new_neighbors.update(conwayAlgHelper(state, deltas, cubeStates, newCubeStates))
        
        for state in new_neighbors:
            conwayAlgHelper(state, deltas, cubeStates, newCubeStates)

        cubeStates = copy.deepcopy(newCubeStates)

    count = 0
    for val in newCubeStates.values():
        if val == '#':
            count += 1
    
    return count


def main():
    cubeStates = readState()
    count = conwayAlg(cubeStates)
    print(count)


if __name__ == "__main__":
    main()