#!/usr/bin/env python3

class Fabric():
    seed = ['.']
    rows = []
    overlap = 0
    no_collisions = []

    def __init__(self):
        self.seed = ['.'] * 1000
        for i in range(1000):
            self.rows.append(self.seed[:])

    def get_location(self, line):
        claim, junk, coords, dimensions = line.split(' ')
        claim = claim.lstrip('#')
        x, y = coords.split(',')
        y = y.rstrip(':')
        run, drop = dimensions.split('x')
        return claim, x, y, run, drop

    def populate(self, claim, x, y, run, drop):
        hits = 0
        for r in range(y, y+drop):
            temprow = self.rows[r]
            for i in range(x, x+run):
                if temprow[i] == '.':
                    temprow[i] = claim
                elif temprow[i] != 'X':
                    self.no_collisions.remove(temprow[i]) if temprow[i] in self.no_collisions else False
                    temprow[i] = 'X'
                    self.overlap += 1
                    hits = 1
                else:
                    hits = 1
        if hits == 0:
            self.no_collisions.append(claim)

    def output(self):
        print("Starting\n---------")
        for r in self.rows:
            print(r)

if __name__ == "__main__":
    fab = Fabric()
    # print(fab.rows[4])

    with open('input.txt') as f:
        infile = f.read().splitlines()
    f.close()
    print("{} Total claims found".format(len(infile)))

    for l, line in enumerate(infile):
        # if l % 50 == 0:
            # print(l)
        claim, x, y, run, drop = fab.get_location(line)
        fab.populate(str(claim), int(x), int(y), int(run),int(drop))
        # fab.output()

    print("{} squares overlap".format(fab.overlap))
    print("Claim {} has no overlap".format(fab.no_collisions[0]))
