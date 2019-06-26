
class QuadVector(object):

    def __init__(self, p):
        self.point = [ int(v) for v in p ]


    def __str__(self):
        v = [ str(x) + "," for x in self.point ]
        return str(v)


    def __getitem__(self,index):
        return self.point[index]


    def __setitem__(self,index, value):
        self.point[index] = value


    def __delitem__(self,index):
        del(self.point[index])


    def mhd(self,p):
        """ Attempt to calculate the Manhattan distance between 2 4D Vectors"""
        # print("Comparing: ", self.point, p, sum(abs(int(ref) - int(check)) for ref, check in zip(self.point, p)))
        return sum(abs(ref - check) for ref, check in zip(self.point, p))
