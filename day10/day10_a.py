#!/usr/bin/env python3
import sys

def readJolts():
    return sorted([int(jolt.strip()) for jolt in sys.stdin.readlines()])

def calcDiff(jolts, valid_jolt_diff):
    curr_jolt = 0
    diff_map = dict()

    for valid_diff in valid_jolt_diff:
        if valid_diff == 3: #Built in adaptor always has a difference of 3
            diff_map[valid_diff] = 1
        else:
            diff_map[valid_diff] = 0

    for jolt in jolts:
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