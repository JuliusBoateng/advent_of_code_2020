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

def getInvalidXmas(xmas, preamble):
    index = preamble
    
    for index in range(preamble, len(xmas)):
        valid_set = validNums(xmas, index - preamble, index)

        if xmas[index] not in valid_set:
            return xmas[index]
    
    return None

def getContigXmas(xmas, invalid_num):
    contig_vals = []

    for index, val in enumerate(xmas):
        if (sum(contig_vals) + val)  < invalid_num:
            contig_vals.append(val)
        elif (sum(contig_vals) + val)  > invalid_num:
            while ( (sum(contig_vals) + val)  > invalid_num) and (len(contig_vals) > 0):
                contig_vals.pop(0)
            
            if (sum(contig_vals) + val)  < invalid_num:
                contig_vals.append(val)
            elif (sum(contig_vals) + val)  == invalid_num:
                return contig_vals + [val]
            else:
                continue
        else:
            return contig_vals + [val]

def main():
    xmas = readXMAS()
    invalid_num = getInvalidXmas(xmas, PREAMBLE)

    if invalid_num != None:
        contig_list = getContigXmas(xmas, invalid_num)
        max_val = max(contig_list)
        min_val = min(contig_list)
        weakness = max_val + min_val
        print(weakness)

if __name__ == "__main__":
    main()