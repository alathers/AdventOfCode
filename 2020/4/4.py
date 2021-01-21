#!/usr/bin/env python3

import re

def validate_data(k,v):
    try:
        if k == 'byr':
            if int(v) >= 1920:
                if int(v) <= 2002:
                    return True
        if k == 'iyr':
            if int(v) >= 2010:
                if int(v) <= 2020:
                    return True
        if k == 'eyr':
            if int(v) >= 2020 and int(v) <= 2030:
                return True
        if k == 'ecl':
            if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return True
        if k == 'pid':
            if len(v) == 9 and re.search('[0-9]',v):
                return True
        if k == 'hgt':
            num = int(v[:-2])
            unit = v[-2:]
            if unit == 'cm' and num >= 150 and num <= 193:
                return True
            if unit == 'in' and num >= 59 and num <= 76:
                return True
        if k == 'hcl':
            if v[0] == '#':
                if len(v) == 7 and re.search('[a-f0-9]{6}', v[1:]):
                    return True
    except:
        return False
    # print("Seems {} = {} failed".format(k,v))
    return False


with open('input.txt') as f:
    infile = f.read().splitlines()


req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
opt_fields = ['cid']

easy_valid = 0
valid = 0
fields = {}

for line in infile:
    if len(line) == 0:
        # new passport, reset fields
        # print(fields)
        diff = set(req_fields).difference(fields.keys())
        # print("Differences: ", diff)
        # print('---')
        if all(elem in fields for elem in req_fields):
            valid += 1
        fields = {}
        continue
    else:
        # all one passport
        passport = line.split(' ')
        for p in passport:
            k,v = p.split(':')
            # print("Checking K {} and V {}".format(k, v))
            if k == 'cid':
                # skip
                continue
            if validate_data(k, v):
                fields[k] = v
            else:
                # print("{} fail for {}".format(k,v))
                # fields = {}
                continue                
        if all(elem in fields for elem in req_fields):
            easy_valid += 1
            valid += 1
            fields = {}
            continue
        # else:
            # print("Differences:  {}", set(req_fields).difference(fields.keys()))
            # print(line)
        # print("{} and {}".format(req_fields, fields))
print(valid)
