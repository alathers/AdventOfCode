#!/usr/bin/env python3

class Fabric():
    seed = ['.']
    rows = []
    overlap = 0

    def __init__(self):
        self.seed = ['.'] * 1000
        self.rows = [self.seed] * 1000

    def get_location(self, line):
        claim, junk, coords, dimensions = line.split(' ')
        claim = claim.lstrip('#')
        x, y = coords.split(',')
        y = y.rstrip(':')
        run, drop = dimensions.split('x')
        return claim, x, y, run, drop

    def populate(self, claim, x, y, run, drop):
        for r in range(y,y+drop):
            row = self.rows[r]
            for i, c in enumerate(self.rows[r]):
                if c != '.':
                    row[i] = claim
                elif c != 'X':
                    row[i] = 'X'
                    self.overlap += 1
                    # print(self.overlap)
            self.rows[r] = row

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
        fab.populate(int(claim), int(x), int(y), int(run),int(drop))

    print("{} squares overlap".format(fab.overlap))
