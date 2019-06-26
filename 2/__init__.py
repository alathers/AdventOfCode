#!/usr/bin/env python3
import numpy as np

with open('input.txt') as f:
    infile = f.read().splitlines()
f.close()

def skim_row(r):
    counter = {}
    row = [0] * len(r)
    print(r)
    print(''.join(sorted(r)))
    for c in r:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    for k in counter:
        if counter[k] > 1:
            row[counter[k]] = 1
    print(row)


def find_repeats(codes):
    rows = []
    for line in codes:
        counter = {}
        row = [0] * len(line)
        for c in line:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        for k in counter:
            if counter[k] > 1:
                row[counter[k]] = 1
        rows.append(row)
        # print(row)
    return rows


row_matrix = find_repeats(infile)

sum_matrix = np.sum(find_repeats(infile), axis=0)



print(sum_matrix)
print(' ')
# skim_row(infile[0])
repeats = 1
for i in sum_matrix:
    if i > 1:
        print(i)
        repeats = repeats * i
print("Repeats: %s" % repeats)
# for r in row_matrix:
#     print(r)