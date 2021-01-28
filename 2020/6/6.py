#!/usr/bin/env python3


with open('input.txt') as f:
    infile = f.read().splitlines()

groups = set()
ys = 0
for g in infile:
    if len(g):
        [groups.add(y) for y in g ]
    else:
        # print(groups, len(groups), ys)
        ys += len(groups)
        groups = set()

# make sure to count the last line    
ys += len(groups)
print(ys)

