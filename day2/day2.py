#!/usr/bin/env python3
import sys

def readPswd():
    if line := sys.stdin.readline():
        policy, pswd = line.split(':')
        pswd = pswd.strip()
        occur, char = policy.split(' ')
        start, stop = map(int, occur.split('-'))
        
        return char, start, stop, pswd
    else:
        return None

def pswdValid(char, start, stop, pswd):
    start = start - 1 # Convert to 0 base index
    stop = stop - 1

    letter1 = pswd[start]
    letter2 = pswd[stop]

    if (letter1 == char) and (letter2 == char):
        return False
    elif (letter1 == char) or (letter2 == char):
        return True
    else:
        return False

def main():
    count = 0
    while(var := readPswd()):
        char, start, stop, pswd = var
        valid = pswdValid(char, start, stop, pswd)
        count += 1 if valid else 0
    
    print(count)

if __name__ == "__main__":
    main()
    