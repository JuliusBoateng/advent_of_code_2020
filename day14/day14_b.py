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
    float_inds = []
    one_inds = []
    offset = len(mask) - 1

    for index, value in enumerate(mask):
        if value == 'X':
            float_inds.append(offset - index)
        
        elif value == '1':
            one_inds.append(offset - index)

    return float_inds, one_inds

def bitOperHelper(mem_key, float_inds):
    if len(float_inds) == 0:
        return [mem_key]
    
    mem_keys = []

    indx = float_inds[0]

    mem_key = mem_key | (1 <<  indx) #1 bit
    mem_keys += bitOperHelper(mem_key, float_inds[1:])

    mem_key = mem_key & ~(1 << indx) #0 bit
    mem_keys += bitOperHelper(mem_key, float_inds[1:])

    return mem_keys

def bitOper(initial_mem_key, float_inds, one_inds):
    for indx in one_inds:
        initial_mem_key = initial_mem_key | (1 <<  indx)
    
    mem_keys = bitOperHelper(initial_mem_key, float_inds)

    return mem_keys
    
def maskData(sysData):
    mem = {}

    for oper in sysData:
        mask = oper[0]
        pairs = oper[1:]
        
        float_inds, one_inds = maskInds(mask)
        
        for pair in pairs:
            initial_mem_key = int(pair[0])
            value = int(pair[1])
            mem_keys = bitOper(initial_mem_key, float_inds, one_inds)
            
            for mem_key in mem_keys:
                mem[mem_key] = value
            
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