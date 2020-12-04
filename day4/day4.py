#!/usr/bin/env python3
import sys

def readPassport():
    passport = []
    
    while (line:= sys.stdin.readline().strip()) != "":
        fields = line.strip().split(' ')
        passport += fields
    
    return passport

def passportValidator(passport, req_set):
    if len(passport) <= 6:
        return False

    for field in passport:
        key, val = field.split(':')

        if key in req_set:
            req_set.remove(key)
    
    return True if (len(req_set) == 0) else False

def main():
    count = 0
    while (passport:= readPassport()):
        req_set = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        val = passportValidator(passport, req_set)

        count += 1 if val else 0
    
    print(count)

if __name__ == "__main__":
    main()