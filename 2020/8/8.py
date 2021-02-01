#!/usr/bin/env python3

instructions = []
acc = 0 
execution_set = set()
# I really should start processing the data as I read it instead of always re-running it a second time
with open('input.txt') as f:
    infile = f.read().splitlines()


for line in infile:
    # print(line)
    line = line.strip()
    op, step = line.split()
    instructions.append([op, int(step)])

i = 0
last_cmd = []
while i < len(instructions) and i not in execution_set:
    # print("looping")
    if instructions[i][0] == 'acc':
        # print(acc, instructions[i][1])
        acc += instructions[i][1]
        last_cmd = [i, instructions[i]]
        execution_set.add(i)
        i += 1
    elif instructions[i][0] == 'nop':
        last_cmd = [i, instructions[i]]
        execution_set.add(i)
        i += 1
    elif instructions[i][0] == 'jmp':
        last_cmd = [i, instructions[i]]
        execution_set.add(i)
        i += instructions[i][1]
    else:
        print("Fault")
        break
    # print(execution_set)

if i == len(instructions):
    print("Victory")

print(i, execution_set)
print(last_cmd)
print(acc)
# print(max(execution_set))