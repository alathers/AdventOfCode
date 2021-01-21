#!/usr/bin/env python3

import re

def validate_data(k,v):
    if k == 'byr':
        if int(v) >= 1920 and int(v) <= 2002:
            return True
        return False
    if k == 'iyr':
        if int(v) >= 2010 and int(v) <= 2020:
            return True
        return False
    if k == 'eyr':
        if int(v) >= 2020 and int(v) <= 2030:
            return True
        return False
    if k == 'ecl':
        if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            return True
        return False
    if k == 'pid':
        if len(v) == 9 and v[0] == '0':
            return True
        return False
    if k == 'hgt':
        return True
    if k == 'hcl':
        return True



with open('input.txt') as f:
    infile = f.read().splitlines()


req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
opt_fields = ['cid']

valid = 0
fields = {}
for line in infile:
    if len(line) == 0:
        # new passport, reset fields
        fields = {}
        continue
    else:
        # all one passport
        passport = line.split(' ')
        for p in passport:
            k,v = p.split(':')
            if validate_data(k, v):
                fields[k] = v
            else:
                fields = []
                continue                
        if all(elem in fields for elem in req_fields) and len(fields) == len(set(fields)):
            valid += 1
            fields = []
            continue
        # print("{} and {}".format(req_fields, fields))
print(valid)