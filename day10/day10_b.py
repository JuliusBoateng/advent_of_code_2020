#!/usr/bin/env python3
import sys

MEMO = dict()

def readJolts():
    jolts = sorted([int(jolt.strip()) for jolt in sys.stdin.readlines()])
    return [0] + jolts + [max(jolts) + 3]

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

def recurDiff(jolts_set, curr):
    if curr == 0:
        return 1

    if curr in MEMO:
        return MEMO[curr]
    
    ways = 0
    for num in range(1,4):
        new_curr = curr - num
        if new_curr in jolts_set:
            ways += recurDiff(jolts_set, new_curr)
        
    MEMO[curr] = ways
    return MEMO[curr]

def main():
    jolts = readJolts()
    jolts_set = set(jolts)
    result = recurDiff(jolts_set, max(jolts))
    print(result)
    # valid_jolt_diff = {1,2,3}
    # diff_map = calcDiff(jolts, valid_jolt_diff)
    # print(diff_map[1] * diff_map[3])
    
if __name__ == "__main__":
    main()