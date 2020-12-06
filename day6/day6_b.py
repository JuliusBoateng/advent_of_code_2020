#!/usr/bin/env python3
import sys
from collections import defaultdict

def groupAnswers():
    group = []

    while (line := sys.stdin.readline()) not in ('\n', ''):
        group.append(line.strip())

    return None if len(group) == 0 else group

def answerCounter(group_answer):
    num_people = len(group_answer)
    char_occurs = defaultdict(int)
    consensus_chars = set()

    for answer in group_answer:
        for char in answer:
            char_occurs[char] += 1

    for char, occur in char_occurs.items():
        if occur == num_people:
            consensus_chars.add(char)
    
    return consensus_chars

def main():
    sum_consensus_chars = 0

    while (group_answer := groupAnswers()):
        consensus_chars = answerCounter(group_answer)
        sum_consensus_chars += len(consensus_chars)
    
    print(sum_consensus_chars)

if __name__ == "__main__":
    main()