#!/usr/bin/env python3
import sys

PREAMBLE = 25

def readXMAS():
    return [int(num.strip()) for num in sys.stdin.readlines()]

def validNums(xmas, start, stop):
    valid_set = set()

    for x in range(start, stop - 1):
        for y in range(x + 1, stop):
            val = xmas[x] + xmas[y]
            valid_set.add(val)

    return valid_set

def invalidXmas(xmas, preamble):
    index = preamble
    
    while index < len(xmas):
        valid_set = validNums(xmas, index - preamble, index)

        if xmas[index] not in valid_set:
            return xmas[index]

        index += 1
    
    return None

def main():
    xmas = readXMAS()
    invalid_num = invalidXmas(xmas, PREAMBLE)
    if invalid_num != None:
        print(invalid_num)

if __name__ == "__main__":
    main()