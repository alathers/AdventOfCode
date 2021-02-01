#!/usr/bin/env python3

import time 
instructions = []
# I really should start processing the data as I read it instead of always re-running it a second time
# with open('sample_input.txt') as f:
with open('input.txt') as f:
    infile = f.read().splitlines()

for line in infile:
    # print(line)
    line = line.strip()
    op, step = line.split()
    instructions.append([op, int(step)])

i = 0
last_cmd = []
toggled = 0
acc = 0 
tested = set()
while i < len(instructions):
    print(i)
    if i == 0:  # Since it can only run once anyway, it's safe to assume I can initalize stuff
        executed = []
    if i in executed:
        print ("Faulting, looping on ", last_cmd)
        print(executed)
        print(tested)
        executed = []
        acc = 0 
        last_cmd = []
        tested.add(toggled)
        toggled = 0 
        i = 0
        # reset
        continue
    # print("looping")
    if instructions[i][0] == 'acc':
        # print(acc, instructions[i][1])
        acc += instructions[i][1]
        last_cmd = [i, instructions[i]]
        executed.append(i)
    elif instructions[i][0] == 'nop':
        if toggled or i in tested or instructions[i][1] == 0 :
            last_cmd = [i, instructions[i]]
            executed.append(i)
        else:  # try swapping this to jump
            last_cmd = [i, instructions[i], 'CHANGED jmp']
            toggled = i
            # tested.add(i)
            executed.append(i)
            i += instructions[i][1]  # do the jump
            continue # don't want the default + 1
    elif instructions[i][0] == 'jmp':
        if toggled or i in tested:
            last_cmd = [i, instructions[i]]
            executed.append(i)
            i += instructions[i][1]
            continue # don't want the default + 1
        else:  # try to make this a nop
            toggled = i
            # tested.add(i)
            last_cmd = [i, instructions[i], 'CHANGED nop']
            executed.append(i)
    else:
        print("Fault")
        break
    # print(execution_set)
    i += 1
    # time.sleep(1)
    


if i == len(instructions):
    print("Victory")

print(i, executed)
print(last_cmd)
print(acc)
