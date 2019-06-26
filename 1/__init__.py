#!/usr/bin/env python3

import operator

ops = { "+": operator.add, "-": operator.sub }

with open('input.txt.txt') as f:
    infile = f.read().splitlines()
f.close()


def sum_freq(lines):
    seen = list()
    uniq_seen = []
    freq = 0
    for z in range(200):
        if z % 10 == 0:
         print(z)
        for line in infile:
            oper = line[0]
            val = int(line[1:])
            freq = ops[oper](freq,val)
            if freq not in seen:
                seen.append(freq)
            else:
                dupe_found = 1
                print("Dupe: ", freq)
                return freq


print(sum_freq(infile))
