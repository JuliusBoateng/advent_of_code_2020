#!/usr/bin/env python3
import sys
import re
from collections import defaultdict

def numParents(child_bag, adj_bag_list, visited):
    if child_bag not in adj_bag_list:
        visited.add(child_bag)
        return visited
    
    for parent_bag in adj_bag_list[child_bag]:
        if parent_bag not in visited:
            visited.add(parent_bag)
            visited.update(numParents(parent_bag, adj_bag_list, visited))

    return visited

def readRules():
    adj_bag_list = defaultdict(dict)

    for rule in sys.stdin.readlines():
        rule_list = [x.strip() for x in re.split(r'contain|,', rule.strip()[:-1])]
        
        if rule_list[1] == "no other bags":
            continue

        parent_bag = rule_list[0]
        
        for rule in rule_list[1:]:
            num, child_bag = rule.split(' ', 1)
            if child_bag[-1] == 'g':
                child_bag += 's'

            adj_bag_list[child_bag][parent_bag] = num
  
    return adj_bag_list

def main():
    adj_bag_list = readRules()
    # print(adj_bag_list)
    num_parents = numParents("shiny gold bags", adj_bag_list, set())
    print(len(num_parents))




if __name__ == "__main__":
    main()