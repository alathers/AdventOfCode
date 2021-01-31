import re

class Bag:
    def __init__(self,desc=None):
        self.description = desc
        self.contains = {}
        self.contained_by = set()


    def getOuterBag(self, s):
        outstring, contents = re.split(' bag[s]{,1} contain', s)
        return outstring


    def setInnerBags(self, s):
        """extract a dict of inner bags
        no other == empty
        no comma == single element
        comma = multi element
        """
        outstring, contents = re.split('contain', s)
        # first special case
        bag_counts = {}
        if not re.match('.*no other bags.*', contents):
            bags = contents.split(',')
            for bag in bags:
                bag = bag.strip()
                number, description = bag.split(' ', 1)
                description = description.replace(' bags','')
                description = description.replace(' bag', '')
                # print(number)
                bag_counts[description] = number
        self.contains = bag_counts


    def populateContains(self, bags):
        for b in bags:
            # If current_bag can contain things (contains is a dict with keys)
            # Then look at each bags object with that key and copy their contains into mine
            inner = {}
            for k in bags[b].contains.keys():
                # print(b, k)
                # return
                inner.update(bags[k].contains)
                for v in inner.keys():
            bags[b].contains.update(inner)


    def canContain(self, desc, bags):
        for bag in bags:
            if desc in bags[bag].contains.keys():
                self.contained_by.add(bags[bag])
        return True


    def containedWithin(self):
        count = 0
        for b in self.contains:
            print(b)
            count += self.contains[b]
        return count

