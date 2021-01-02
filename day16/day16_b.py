#!/usr/bin/env python3
import sys
from collections import defaultdict
from copy import deepcopy
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
            
            rule = []
            for match in matches:
                match = (int(match[0]), int(match[1]))
                rule.append(match)
                
            rules.append(rule)
        
        elif context == "my_ticket":
            my_ticket = [int(num) for num in line.split(',')]
        
        else:
            ticket = [int(num) for num in line.split(',')]
            other_tickets.append(ticket)

    return rules, my_ticket, other_tickets

def validTicket(rules, ticket):
    for val in ticket:
        for rule in rules:
            valid = False

            for tup in rule:
                if (val >= tup[0]) and (val <= tup[1]):
                    valid = True
                    break

            if valid:
                break
        
        if not valid:
            return False

    return True

def applyRulesHelper(order, rules, ticket):
    for ticket_index, val in enumerate(ticket):
        for rule_index, rule in enumerate(rules):
            valid = False

            for tup in rule:
                if (val >= tup[0]) and (val <= tup[1]):
                    valid = True
                    break
        
            if not valid:
                order[rule_index].discard(ticket_index)

def applyRules(rules, other_tickets):
    order = defaultdict(set)

    for rule_index in range(len(rules)): 
        for ticket_index in range(len(other_tickets[0])):
            order[rule_index].add(ticket_index)

    for ticket in other_tickets:
        if not validTicket(rules, ticket):
            continue

        applyRulesHelper(order, rules, ticket)
    
    return order

def matchPosHelper(order):
    len_order = defaultdict(set)

    for rule_index, ticket_indexes in order.items():
        len_index = len(ticket_indexes)
        len_order[len_index].add(rule_index)

    return len_order

def matchPos(order):
    visited_index = set()

    len_order = matchPosHelper(order)
    for len_key in sorted(len_order.keys()):
        for val_key in len_order[len_key]:
            tickets = deepcopy(order[val_key])
            for val in tickets:
                if val in visited_index:
                    order[val_key].remove(val)
                else:
                    visited_index.add(val)

def ticketVals(fields_index_list, order, my_ticket):
    matchPos(order)
    result = []
    
    for val in fields_index_list:
        index = order[val].pop()
        result.append(my_ticket[index])

    return result

def main():
    rules, my_ticket, other_tickets = readNotes()
    order = applyRules(rules, other_tickets)
    vals = ticketVals([0,1,2,3,4,5], order, my_ticket)

    mult = 1
    for val in vals:
        mult = mult * val
    
    print(mult)
    
if __name__ == "__main__":
    main()