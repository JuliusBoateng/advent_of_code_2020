#!/usr/bin/env python3
import sys
from re import findall

def readNotes():
    context = "Rules"
    rules = []
    my_ticket = []
    other_tickets = []

    while line := sys.stdin.readline():
        if line == "\n":
            continue

        line = line.strip()

        if line == "your ticket:":
            context = "my_ticket"
            continue
        
        if line == "nearby tickets:":
            context = "other_tickets"
            continue
        
        if context == "Rules":
            matches = findall(r"(\d+)-(\d+)", line)
            
            for match in matches:
                match = (int(match[0]), int(match[1]))
                rules.append(match)
        
        elif context == "my_ticket":
            my_ticket = [int(num) for num in line.split(',')]
        
        else:
            ticket = [int(num) for num in line.split(',')]
            other_tickets.append(ticket)

    return rules, my_ticket, other_tickets

def invalidNums(rules, ticket):
    invalid_vals = []

    for val in ticket:
        valid = False

        for rule in rules:
            if (val >= rule[0]) and (val <= rule[1]):
                valid = True

        if not valid:
            invalid_vals.append(val)

    return invalid_vals if len(invalid_vals) > 0 else None

def applyRules(rules, other_tickets):
    error_rate = 0

    for ticket in other_tickets:
        invalid_vals = invalidNums(rules, ticket)

        if invalid_vals:
           for vals in invalid_vals:
               error_rate += vals
    
    return error_rate

def main():
    rules, my_ticket, other_tickets = readNotes()
    error_rate = applyRules(rules, other_tickets)
    print(error_rate)

if __name__ == "__main__":
    main()