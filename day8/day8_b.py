#!/usr/bin/env python3
import sys
from copy import deepcopy

def readInstr():
    result = []
    for instr in sys.stdin.readlines():
        oper, arg = instr.split()
        arg = int(arg)
        result.append([oper,arg])

    return result

def playInstr(instr, start_index, swap, visited_instr):
    num_instr = len(instr)
    index = start_index

    acc = 0
    while (index < num_instr) and (index >= 0) and (index not in visited_instr):
        copy_visited_instr = deepcopy(visited_instr)
        visited_instr.add(index)
        
        if instr[index][0] == "acc":
            acc += instr[index][1]
            index += 1
        elif instr[index][0] == "jmp":
            if not swap:
                new_instr = instr[:index] + [["nop", instr[index][1]]] + instr[index + 1:]
                val = playInstr(new_instr, index, True, copy_visited_instr)

                if val != None:
                    return acc + val
            
            index += instr[index][1]
        else:
            if not swap:
                new_instr = instr[:index] + [["jmp", instr[index][1]]] + instr[index + 1:]
                val = playInstr(new_instr, index, True, copy_visited_instr)
                
                if val != None:
                    return acc + val

            index += 1

    return acc if index >= num_instr else None

def main():
    instr = readInstr()
    acc = playInstr(instr, 0, False, set())
    print(acc)

if __name__ == "__main__":
    main()