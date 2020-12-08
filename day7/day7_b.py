#!/usr/bin/env python3
import sys
import re
from collections import defaultdict

def getChildren(parent_bag, adj_bag_list):
    if len(adj_bag_list[parent_bag]) == 0:
        return 0
    
    count = 0
    for child_bag in adj_bag_list[parent_bag]:
        val = adj_bag_list[parent_bag][child_bag]
        count += val
        count += val * getChildren(child_bag, adj_bag_list)
    
    return count

def readRules():
    adj_bag_list = defaultdict(dict)

    for rule in sys.stdin.readlines():
        rule_list = [x.strip() for x in re.split(r'contain|,', rule.strip()[:-1])]
        parent_bag = rule_list[0]

        if rule_list[1] == "no other bags":
            adj_bag_list[parent_bag] #defaultdict
        else:
            for rule in rule_list[1:]:
                num, child_bag = rule.split(' ', 1)
                if child_bag[-1] == 'g':
                    child_bag += 's'

                adj_bag_list[parent_bag][child_bag] = int(num)
  
    return adj_bag_list

def main():
    adj_bag_list = readRules()
    num_children = getChildren("shiny gold bags", adj_bag_list)
    print(num_children)




if __name__ == "__main__":
    main()