#!/usr/bin/env python3
import sys

def readInstr():
    result = []
    for instr in sys.stdin.readlines():
        oper, arg = instr.split()
        arg = int(arg)
        result.append([oper,arg])

    return result

def playInstr(instr):
    num_instr = len(instr)
    visited_instr = set()

    index = 0
    count = 0
    acc = 0
    while (index < num_instr) and (index not in visited_instr):
        visited_instr.add(index)
        count+=1
  
        if instr[index][0] == "acc":
            acc += instr[index][1]
            print(f"Order: {count} {instr[index]}")
            print(index)
            index += 1
        elif instr[index][0] == "jmp":
            print(f"Order: {count} {instr[index]}")
            print(index)
            index += instr[index][1]
        else:
            print(f"Order: {count} {instr[index]}")
            print(index)
            index += 1
    
    return acc

def main():
    instr = readInstr()
    acc = playInstr(instr)
    print(acc)


if __name__ == "__main__":
    main()