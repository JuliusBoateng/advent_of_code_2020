#!/usr/bin/env python3
import sys

GOAL = 2020

def dict_pairs(lines):
    dic = dict()

    for index_1 in range(len(lines) - 1):
        for index_2 in range(index_1, len(lines)):
            val = GOAL - (lines[index_1] + lines[index_2])
            
            if val > 0:
                dic[val] = [lines[index_1], lines[index_2]]

    return dic

def sum_to_2020(lines, dic):
    lines_set = set(lines)

    for val in dic:
        if val in lines_set:
            return val * dic[val][0] * dic[val][1]

def main():
    lines = list(map(lambda num: int(num.strip()),sys.stdin))
    dic = dict_pairs(lines)
    print(sum_to_2020(lines, dic))

if __name__ == "__main__":
    main()