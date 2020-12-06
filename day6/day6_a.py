#!/usr/bin/env python3
import sys

def groupAnswers():
    group = []

    while (line := sys.stdin.readline()) not in ('\n', ''):
        group.append(line.strip())

    return None if len(group) == 0 else group

def answerCounter(group_answer):
    unique_chars = set()

    for answer in group_answer:
        for char in answer:
            unique_chars.add(char)

    return unique_chars

def main():
    sum_unique_chars = 0

    while (group_answer := groupAnswers()):
        unique_chars = answerCounter(group_answer)
        sum_unique_chars += len(unique_chars)
    
    print(sum_unique_chars)




if __name__ == "__main__":
    main()