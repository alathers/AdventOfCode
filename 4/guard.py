

# For each guard you need to track:
# tally of each minute they sleep each day they work
# total minutes slept
class Guard(object):

    def __init__(self, id=None):
        self.id = id
        self.sleep = 0
        self.minutes = [0] * 60


    def tally(self, start, end):
        # print("Servicing tally on {} , {} {} {}".format(self.id, start, end, self.sleep))
        sleep = start - end
        self.sleep += sleep
        for i in range(end,start-1):
            self.minutes[i] += 1

    def sleepiest_minute(self):
        max_sleep = max(self.minutes)
        # print(self.minutes.index(max_sleep))
        return int(self.minutes.index(max_sleep))


class Guards(Guard):

    def __init__(self):
        self.max_sleep = -1
        self.sleepiest_guard = -1
        self.sleepiest_minute = -1
        self.guards = dict()

    def tally_guard(self, id, start, end):
        try:
            self.guards[id]
        except:
            self.guards[id] = Guard(id)
        self.guards[id].tally(start,end)
        if self.sleepiest_guard > 0 and self.guards[id].sleep > self.guards[self.sleepiest_guard].sleep:
            self.sleepiest_guard = id
        elif self.sleepiest_guard == -1:
            self.sleepiest_guard = id
        try:
            self.sleepiest_minute = self.guards[self.sleepiest_guard].sleepiest_minute()
        except:
            pass


    def dump_guards(self):
        for g in self.guards:
            gd = self.guards[g]
            # print(gd.__dict__)
            print("{} {}  {}".format(g, gd.sleep, gd.sleepiest_minute()))