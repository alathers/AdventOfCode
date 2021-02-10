#!/usr/bin/env python3

from collections import deque
import math 

def check_val(d, v):
    for s in d:
        if v in s:
            return True
    return False
    
with open('input.txt') as f:
# with open('sample_input.txt') as f:
    infile = list(map(int, f.read().splitlines()))

preamble_window = 25
# preamble_window = 5
window = deque(maxlen=preamble_window)
sums = deque(maxlen=preamble_window)

# setup
for i in range(preamble_window):
    window.append(int(infile[i]))

# print(window)
#generate list of sums

for i in range(preamble_window):
    pair_sums = [window[i] + window[j] for j in range(preamble_window) if i != j ] 
    sums.append(pair_sums)
# print(sums)
# print('STEPPING')

for i in range(preamble_window,len(infile)):
    if not check_val(sums, int(infile[i])):
        print(int(infile[i]), "Not found")
        breaker = int(infile[i])
        break_index = i
        # print(window)
        # print(sums)
        break
    else:
        # print("sliding window")
        window.popleft()
        pair_sums = [int(infile[i]) + window[j] for j in range(len(window)) ]
        sums.append(pair_sums)
        window.append(int(infile[i]))
        # print(window)
        # print(sums)

running_sum = 0 
i = 0
done = 0
while i < len(infile) and done != 1:
    j = i + 1
    while j < len(infile):
        # print(j)
        if sum(infile[i:j]) == breaker:
            done = 1
            print(min(infile[i:j]), max(infile[i:j]), min(infile[i:j]) + max(infile[i:j]))
            break
        elif sum(infile[i:j]) > breaker:
            break
        else:
            j += 1
    i += 1
