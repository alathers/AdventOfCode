

# For each guard you need to track:
# tally of each minute they sleep each day they work
# total minutes slept
class Guard(object):

    def __init__(self, id=None):
        self.id = id
        self.sleep = 0
        self.minutes = [0] * 60
        self.minute_hashes = ["-"] * 60

    def tally(self, rest, wake):
        # print("Servicing tally on {} , {} {} {}".format(self.id, start, end, self.sleep))
        sleep = wake - rest
        self.sleep += sleep
        # print(rest, wake)
        for i in range(rest, wake):
            # print(i)
            self.minutes[i] += 1

    def sleepiest_minute(self):
        max_sleep = max(self.minutes)
        # print(self.minutes.index(max_sleep))
        return int(self.minutes.index(max_sleep))


class Guards(Guard):

    def __init__(self):
        self.max_sleep = -1
        self.sleepiest_guard = None
        self.sleepiest_minute = -1
        self.guards = dict()

    def tally_guard(self, id, rest, end):
        try:
            self.guards[id]
        except:
            self.guards[id] = Guard(id)
        self.guards[id].tally(rest, end)

    def sleepiest(self):
        guards = self.guards
        g_max = max ( guards, key=lambda x: guards[x].sleep)
        return guards[g_max]

    def dump_guards(self):
        for g in self.guards:
            gd = self.guards[g]
            # print(gd.__dict__)
            print("{} {}  {}".format(g, gd.sleep, gd.sleepiest_minute()))

    def absolute_sleepiest_minute(self):
        guards = self.guards
        g_max = max ( guards, key=lambda x: guards[x].minutes[guards[x].sleepiest_minute()])
        return guards[g_max]

    def dump_guard_minutes(self):
        for g in self.guards:
            gd = self.guards[g]
            # print(gd.__dict__)
            print("{} {}  {}".format(g, gd.sleep, gd.sleepiest_minute()))
            print("{}".format(gd.minutes))



"""
Guests Part 1
68183
61531
35184   <-


Guest Part 2
35472
11824
35472

37886  <-
"""