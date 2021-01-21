#!/usr/bin/env python3


with open('input.txt') as f:
    infile = f.read().splitlines()


req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
opt_fields = ['cid']

valid = 0
for line in infile:
    passport = line.split(' ')
    if len(passport) < len(req_fields):
        # print('skip")')
        continue
    else:
        fields = []
        for p in passport:
            k,v = p.split(':')
            fields.append(k)
        if all(elem in fields for elem in req_fields):
            valid = valid + 1
        # print("{} and {}".format(req_fields, fields))
print(valid)