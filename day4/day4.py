#!/usr/bin/env python3
import sys
from re import fullmatch, match

def readPassport():
    passport = []
    
    while (line:= sys.stdin.readline().strip()) != "":
        fields = line.strip().split(' ')
        passport += fields
    
    return passport

def fieldValidator(key, val):
    if key == "byr":
        return True if val.isnumeric() and (int(val) >= 1920) and (int(val) <= 2002) else False

    if key == "iyr":
        return True if val.isnumeric() and (int(val) >= 2010) and (int(val) <= 2020) else False

    if key == "eyr":
        return True if val.isnumeric() and (int(val) >= 2020) and (int(val) <= 2030) else False

    if key == "hgt":
        if fullmatch(r'(\d*)(cm)', val):
            expr = match(r'\d*', val)
            num = int(expr[0])

            return True if (num >= 150) and (num <= 193) else False
        
        if fullmatch(r'(\d*)(in)', val):
            expr = match(r'\d*', val)
            num = int(expr[0])
   
            return True if (num >= 59) and (num <= 76) else False

        return False

    if key == "hcl":
        return True if fullmatch(r'#(\d|[a-f]){6}', val) else False

    if key == "ecl":
        return True if fullmatch(r'(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)', val) else False

    if key == "pid":
        return True if fullmatch(r'\d{9}', val) else False

    return False


def passportValidator(passport, req_set):
    if len(passport) <= 6:
        return False

    for field in passport:
        key, val = field.split(':')
        valid = fieldValidator(key, val)

        if valid and (key in req_set):
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