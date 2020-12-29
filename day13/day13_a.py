#!/usr/bin/env python3
import sys

def readTimeStamp():
    time = int(sys.stdin.readline())
    idSet = set()

    for val in sys.stdin.readline().split(','):
        if val != 'x':
            idSet.add(int(val))
    
    return time, idSet

def earliestID(time, idSet):
    minTime = float('inf')
    minID = -1
    minDiff = 0

    for busID in idSet:
        if (time % busID) == 0:
            return busID
        else:
            diff = time % busID
            calcTime = time + busID - diff

            if calcTime < minTime:
                minTime = calcTime
                minID = busID
                minDiff = minTime - time
    
    return minID, minDiff


def main():
    time, idSet = readTimeStamp()
    minID, minDiff = earliestID(time, idSet)
    print(minID * minDiff)

if __name__ == "__main__":
    main()