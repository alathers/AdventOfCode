#!/usr/bin/env python3
import math

# Part 1: For map file, if down/right is tree, increment count


with open('input.txt') as f:
    infile = f.read().splitlines()

# loop over each row
trees = [0, 0, 0, 0, 0]
col = [0, 0, 0, 0, 0]
right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]
for n, line in enumerate(infile):
    # Part 1
    # col = (col + right) % len(line)
    # if n + down < len(infile) and infile[n+down][col] == '#':
    #     trees += 1

    # for d in down:
    #     if n % d == 0:
    #         # Eval this pass
    for k,c in enumerate(col):
        print(k,c)
        if (n % down[k]) != 0:
            # print('skip')
            # Skip this check if you step past it via slope
            continue
        else:
            col[k] = (col[k] + right[k]) % len(line)
            print(col[k])
            downstep = n + down[k]
            if downstep < len(infile):
                charcheck = infile[downstep][col[k]]
                if charcheck == '#':
                    print('tree bump')
                    trees[k] = trees[k] + 1


print(trees)
print(math.prod(trees))