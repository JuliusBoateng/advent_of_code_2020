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

def main():
    jolts = readJolts()
    valid_jolt_diff = {1,2,3}
    diff_map = calcDiff(jolts, valid_jolt_diff)
    print(diff_map[1] * diff_map[3])
    
if __name__ == "__main__":
    main()