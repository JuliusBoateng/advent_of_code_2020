#!/usr/bin/env python3
import sys
from re import fullmatch

def readSys():
    sysData = []

    while line := sys.stdin.readline().strip():
        mask = fullmatch(r"(mask = )(.+)", line)

        if mask != None:
            mask = mask.groups()[1]
            sysData.append([mask])
        else:
            data = fullmatch(r"(mem\[(\d+)\]) = (\d+)", line)
            data = data.groups()[1:]
            sysData[-1].append(data)

    return sysData

def maskInds(mask):
    zero_inds = []
    one_inds = []
    offset = len(mask) - 1

    for index, value in enumerate(mask):
        if value == 'X':
            continue
        
        elif value == '1':
            one_inds.append(offset - index)

        else:
            zero_inds.append(offset - index)

    return zero_inds, one_inds

def bitOper(value, zero_inds, one_inds):
    for indx in one_inds:
        value = value | (1 <<  indx)
    
    for indx in zero_inds:
        value = value & ~(1 << indx)
    
    return value
    
def maskData(sysData):
    mem = {}

    for oper in sysData:
        mask = oper[0]
        pairs = oper[1:]
        
        zero_inds, one_inds = maskInds(mask)
        
        for pair in pairs:
            mem_key = int(pair[0])
            value = int(pair[1])
            new_value = bitOper(value, zero_inds, one_inds)
            mem[mem_key] = new_value
        
    return mem

def memSum(mem):
    total = 0

    for val in mem.values():
        total += val

    return total
        
def main():
    sysData = readSys()
    mem = maskData(sysData)
    total = memSum(mem)
    print(total)

if __name__ == "__main__":
    main()