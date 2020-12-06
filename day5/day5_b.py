#!/usr/bin/env python3
import sys

NUM_ROWS = 128
NUM_COLS = 8
ROW_MULT = 8

def boardingPasses():
    return [line.strip() for line in sys.stdin.readlines()]

def binaryPartition(start, stop, char):
    mid = (start + stop)//2

    if char == 'F' or char == 'L':
        return (start, mid)
    else:
        return (mid+1, stop)

def seatPosition(board_pass):
    pass_row = board_pass[:7]
    row_start = 0
    row_stop = NUM_ROWS - 1 #0 based index

    pass_col = board_pass[7:]
    col_start = 0
    col_stop = NUM_COLS - 1
    
    for char in pass_row:
        row_start, row_stop = binaryPartition(row_start, row_stop, char)
    
    for char in pass_col:
        col_start, col_stop = binaryPartition(col_start, col_stop, char)
    
    return row_start, col_start

def seatID(row, col):
    return row * ROW_MULT + col

def missingID(ids):
    for index in range( len(ids) - 1 ):
        if (ids[index] + 1) != ids[index + 1]:
            return ids[index] + 1

def main():
    ids = []
    board_passes = boardingPasses()
  
    for board_pass in board_passes:
        row, col = seatPosition(board_pass)
        ids.append(seatID(row,col))

    seat_id = missingID(sorted(ids))
    print(seat_id)


if __name__ == "__main__":
    main()