#!/usr/bin/env python3

from guard import Guard,Guards

# Start simple, this is all during the same hour so it's just minutes - minutes
# also super naive assumptions, they fall asleep before they wake

def custom_sort(t):
    return t[1:10]

with open('all_input.txt') as f:
    infile = f.read().splitlines()
f.close()

infile.sort(key=custom_sort)

guards = Guards()

for line in infile:
    # print("{}".format(line))
    if 'Guard' in line:
        day, time, group, num, rem, rem2 = line.split(' ')
        guard = int(num[1:])
        # print("Setting guard {}".format(guard))
    else:
        day, time, act, other = line.split(' ')
        hh, mm = time.split(':')
        mm = mm.replace(']', '')
        if act == 'falls':
            if hh == '00':
                # only counting starting at midnight
                rest = int(mm)
            else:
                # print("shifting to start at midnight")
                rest = 0
            wake = None
            # print("tracking rest starting at {}".format(rest))
        elif act == 'wakes':
            if hh == '00':
                wake = int(mm)
            else:
                # print("shifting to end before midnight")
                wake = 59
            # print("tracking wake starting at {}".format(wake))
        try:
            rest
            wake
            guard
            if wake is not None and rest is not None:
                # print("Adding minutes from {} to {} for {}".format(rest, wake, guard))
                guards.tally_guard(guard, rest, wake)
                rest = None
                wake = None
        except NameError:
            # print("Exception hit")
            pass


# sleepiest = guards.sleepiest_guard
# minute = guards.sleepiest_minute
# total = sleepiest * minute

sleepy_guard = guards.sleepiest()
sleepiest_minute = sleepy_guard.sleepiest_minute()
print(sleepy_guard.id)
print(sleepiest_minute)
print(sleepy_guard.id * sleepiest_minute)
print()

# print("{} {} {}".format(sleepy_guard.id, sleepy_guard.sleepiest_minute,
#                         sleepy_guard.id * sleepy_guard.sleepiest_minute ))
# print("{} {} {}".format(sleepiest,minute,total))
# print("{}".format(guards[guards.sleepiest_guard()].sleep))
# guards.dump_guards()

# print( [ (k,v) for (k,v) in enumerate(guards.guards[sleepiest].minutes) ])
guard_with_max_hits = guards.absolute_sleepiest_minute()
absolute_sleepiest_minute = guard_with_max_hits.sleepiest_minute()
times_on_minute = guard_with_max_hits.minutes[absolute_sleepiest_minute]
which_minute = guard_with_max_hits.minutes.index(times_on_minute)
print('---')
print(guard_with_max_hits.id)
print(absolute_sleepiest_minute)
print(times_on_minute)
print(which_minute)
print(guard_with_max_hits.id * which_minute)
print()

guards.dump_guard_minutes()