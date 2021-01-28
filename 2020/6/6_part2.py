#!/usr/bin/env python3


with open('input.txt') as f:
    infile = f.read().splitlines()

group = []
yeses = 0
for n,g in enumerate(infile):
    if len(g):
        group.append(g)
    if len(g) == 0 or n == len(infile)-1:
        result = ''
        for s in group:
            if not result:
                result = set([c for c in s])
            else:
                result = set([c for c in s]).intersection(result)
        # print(result,len(result), ys)
        yeses += len(result)
        last = result
        print(yeses, last)
        result = ''
        group = []

yeses += len(last)
print(yeses)