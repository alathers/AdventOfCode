#!/usr/bin/env python3

from guard import Guard,Guards

# Start simple, this is all during the same hour so it's just minutes - minutes
# also super naive assumptions, they fall asleep before they wake

def custom_sort(t):
    return t[1:10]

with open('input.txt') as f:
    infile = f.read().splitlines()
f.close()

infile.sort(key=custom_sort)

guards = Guards()

for line in infile:
    if 'Guard' in line:
        day, time, group, num, rem, rem2 = line.split(' ')
        guard = int(num[1:])
    else:
        day, time, act, other = line.split(' ')
        hh, mm = time.split(':')
        mm = mm.replace(']', '')
        if act == 'falls':
            stop = int(mm)
        elif act == 'wakes':
            start = int(mm)
        try:
            start
            stop
            guard
            if stop is not None and start is not None:
                guards.tally_guard(guard, start, stop)
                start = None
                stop = None
        except NameError:
            print("Exception hit")



sleepiest = guards.sleepiest_guard
minute = guards.sleepiest_minute
total = sleepiest * minute
print("{} {} {}".format(sleepiest,minute,total))
# print("{}".format(guards[guards.sleepiest_guard()].sleep))
guards.dump_guards()

