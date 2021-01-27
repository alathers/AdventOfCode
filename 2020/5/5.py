#!/usr/bin/env python3
#
#  Adam Lathers alathers@gmail.com
#

'''
problem:
part 1:
    for each ticket, calculate the seat_id, which is (row * 8) + col
    report max
'''
import math
with open('input.txt') as f:
    infile = f.read().splitlines()

# I don't actually need to store anything I don't think
# as the problem space is extremely well defined


# I don't *yet* have to do recursion either I think?
max_seat = 0
for line in infile:
    rowstring = ''
    colstring = ''
    for c in line[::]:
        if c == 'F':
            rowstring += '0'
        elif c == 'B':
            rowstring += '1'
        elif c == 'L':
            colstring += '0'
        elif c == 'R':
            colstring += '1'
        else:
            print(c)
    # print(int(rowstring,2))
    # print(int(rowstring, 2) * 8 + int(colstring, 2))
    # print(line, rowstring, colstring)
    max_seat = max(max_seat, (int(rowstring, 2) * 8 + int(colstring, 2)))
    

print(max_seat)
# print(row)

