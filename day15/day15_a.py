#!/usr/bin/env python3
import sys

def readNums():
    return [int(num) for num in sys.stdin.readline().split(',')]

def calcNum(arrNums, nth_num):
    dicNums = {}

    for index, num in enumerate(arrNums):
        dicNums[num] = index
    
    for index in range(len(dicNums), nth_num):
        prev_index = index - 1
        prev_val = arrNums[prev_index]
        if prev_val not in dicNums:
            dicNums[prev_val] = prev_index

        prev_val_index = dicNums[prev_val]

        curr_val = prev_index - prev_val_index
        dicNums[prev_val] = prev_index

        arrNums.append(curr_val) 

    return arrNums[-1]

def main():
    arrNums = readNums()
    nth_val = calcNum(arrNums, 2020)
    print(nth_val)



if __name__ == "__main__":
    main()