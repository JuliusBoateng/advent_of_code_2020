#!/usr/bin/env python3
import sys

def readJolts():
    return sorted([int(jolt.strip()) for jolt in sys.stdin.readlines()])

def calcDiff(jolts, valid_jolt_diff):
    diff_map = {1: 0, 2: 0, 3:0}
    curr_jolt = 0

    for jolt in jolts[1:]:
        diff = jolt - curr_jolt
        if diff not in valid_jolt_diff:
            break

        diff_map[diff] += 1
        curr_jolt = jolt

    return diff_map

def joltTable(diff_map, jolts_total, jolts):
    jolts_set = set(jolts)
    table = [[0 for col in range(jolts_total + 1)] for row in range(len(diff_map) + 1)]

    for row in range(len(diff_map) + 1): #Initializing empty set
        table[row][0] = 1

    for row in range(1, len(diff_map) + 1):
        for col in range(1, jolts_total + 1):
            if col not in jolts_set:
                continue

            val = 0
            new_col = col - row
            if new_col >= 0:
                while new_col not in jolts_set:
                    new_col -= 1
                
                val += table[row][new_col]
            
            val += table[row - 1][col]
            table[row][col] = val

    print(table)


def main():
    jolts = readJolts()
    jolts = [0] + jolts + [jolts[-1] + 3]

    valid_jolt_diff = {1,2,3}
    diff_map = calcDiff(jolts, valid_jolt_diff)

    jolts_total = 0
    for key, val in diff_map.items():
        jolts_total += key * val
    
    print(jolts_total)
    print(jolts)
    joltTable(diff_map, jolts_total, jolts)

if __name__ == "__main__":
    main()