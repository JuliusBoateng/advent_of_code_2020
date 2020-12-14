#!/usr/bin/env python3
import sys

def readJolts():
    return sorted([int(jolt.strip()) for jolt in sys.stdin.readlines()])

def calcDiff(jolts, valid_jolt_diff):
    diff_map = {1: 0, 2: 0, 3:0}
    new_jolts = [0] + jolts + [jolts[-1] + 3]
    curr_jolt = 0

    for jolt in new_jolts[1:]:
        diff = jolt - curr_jolt
        if diff not in valid_jolt_diff:
            break

        diff_map[diff] += 1
        curr_jolt = jolt

    return diff_map

def joltTable(diff_map, jolts_total):
    table = [[0 for col in range(jolts_total + 1)] for row in range(len(diff_map) + 1)]

    for row in range(len(diff_map) + 1): #Initializing empty set
        table[row][0] = 1

    for row in range(1, len(diff_map) + 1):
        for col in range(1, jolts_total + 1):
            val = 0
            if col - row >= 0:
                val += table[row][col - row]
            
            val += table[row - 1][col]
            table[row][col] = val

    print(table)


def main():
    jolts = readJolts()
    valid_jolt_diff = {1,2,3}
    diff_map = calcDiff(jolts, valid_jolt_diff)
    print(diff_map)

    jolts_total = 0
    for key, val in diff_map.items():
        jolts_total += key * val
    
    print(jolts_total)
    joltTable(diff_map, jolts_total)

if __name__ == "__main__":
    main()