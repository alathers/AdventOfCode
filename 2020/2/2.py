#!/usr/bin/env python3

"""
Part 1:
For each line:
4-5 m: lklqm
min-max char: pass

count number of valid passwords
"""

with open('input.txt') as f:
    infile = f.read().splitlines()

partone_valid = {}
parttwo_valid = {}

for line in infile:
    info,passwd = line.split(':')
    passwd = passwd.strip()  # Stupid whitespace!
    info = info.split()
    mincheck,maxcheck = map(int, info[0].split('-'))
    # print(info[1])
    req_counter = 0
    for i in passwd:
        if i == info[1]:
            req_counter += 1
    if req_counter >= mincheck and req_counter <= maxcheck:
        partone_valid[passwd] = line
    if passwd[mincheck-1] != passwd[maxcheck-1]:
        if passwd[mincheck-1] == info[1] or passwd[maxcheck-1] == info[1]:
            parttwo_valid[passwd] = line
            print("Checking {} index {} and {} index {} as equal to {} for passwd -{}- ".format(
                passwd[mincheck-1], mincheck-1, passwd[maxcheck-1], maxcheck-1, info[1], passwd))
            

print("Part One Valid: {}".format(len(partone_valid.keys())))
print("Part Two Valid: {}".format(len(parttwo_valid .keys())))
# print(parttwo_valid)
