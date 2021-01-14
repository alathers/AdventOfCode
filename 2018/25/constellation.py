#!/usr/bin/env python3

from quad_vector import QuadVector

class Constellation(object):
    """Basically this is a list of points, start with 4 per list"""


    def __init__(self):
        """A list of QuadVector objects"""
        self.points = list()


    def __getitem__(self,index):
        return self.points[index]


    def __setitem__(self,index, value):
        self.points[index] = value


    def __delitem__(self,index):
        del(self.points[index])


    def add_point(self, qv):
        self.points.append(qv)
        return


    def check_reach(self, max_reach, qv):
        for p in self.points:
            # print(p, qv, (p.mhd(qv)))
            if int(p.mhd(qv)) <= int(max_reach):
                self.add_point(qv)
                return True
        return False



class Constellations(Constellation):
    """A List of Constellation Objects"""


    def __init__(self, max_mhd):
        self.max_mhd = max_mhd
        self.constellations = list()

    def __getitem__(self,index):
        return self.constellations[index]


    def __setitem__(self,index, value):
        self.constellations[index] = value


    def __delitem__(self,index):
        del(self.constellations[index])

    def count(self):
        return len(self.constellations)

    def count_all(self):
        for c in self.constellations:
            print ("%s", len(c))

    def merge_down(self, frm, into):
        # print("Merging %i %i", frm, into)
        self.constellations[into].points = self.constellations[into].points + self.constellations[frm].points
        del(self.constellations[frm])


    def nova(self, qv):
        """Create new constellation and append first point"""
        # print("New Constellation, first quad", qv)
        c = Constellation()
        c.add_point(qv)
        # print("Length: ", self.count()+1)
        self.constellations.append(c)


#### This is the flaw, I need to be able to merge them if I find bridging points out of order
    def explore(self, qv):
        """Lazily assume this will either hit, or add a new Constellation"""
        if len(qv.point) < self.max_mhd:
            return
        index_save = -1
        for i, c in enumerate(self.constellations):
            if c.check_reach(self.max_mhd, qv) is True:
                # print("Found match ", i)
                if index_save == -1:
                    index_save = i
                else:
                    self.merge_down(i, index_save)
        if index_save != -1:
            return
        self.nova(qv)
