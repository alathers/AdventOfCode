#!/usr/bin/env python3
import numpy as np
import difflib


def skim_row(r):
    counter = {}
    row = [0] * len(r)
    for c in r:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    for k in counter:
        if counter[k] > 1:
            row[counter[k]] = 1

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
    return rows

def compare(infile):
    clip_flip = infile[:]
    for l, line in enumerate(infile):
        # print("Testing Line {}".format(l))
        for i, line2 in enumerate(clip_flip):
            # print("{}\n{}\n------".format(line,line2))
            diff_chars = 0
            save_diff = ''
            for a,b in zip(line, line2):
                if a == b:
                    continue
                elif diff_chars > 1:
                    break
                else:
                    save_diff = l
                    diff_chars += 1
            if diff_chars == 1:
                return line, line2



if __name__ == "__main__":
    with open('input.txt') as f:
        infile = f.read().splitlines()
    f.close()
    ### Part 1
    print("Starting Line Count %s" % len(infile))
    row_matrix = find_repeats(infile)
    sum_matrix = np.sum(find_repeats(infile), axis=0)
    repeats = 1
    for i in sum_matrix:
        if i > 1:
            repeats = repeats * i
    print("Checksum: %s" % repeats)

    ### Part 2
    line1, line2 = compare(infile)
    print("Close Match 1  {}\nClose Match 2  {}".format(line1, line2))
    for c in range(len(line1)):
        if line1[c] != line2[c]:
            print("Diff:          {}".format(line1[:c] + line1[c+1:]))


