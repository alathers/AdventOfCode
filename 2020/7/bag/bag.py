import re

class Bag:
    def __init__(self,desc=None):
        # String for the name of the bag
        self.description = desc
        # A dict of bag names and counts for what this can contain
        self.contains = {}
        # A set of strings for the bags that can contain this bag.
        self.contained_by = set()
        self.nested_bags = 0


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
                bag_counts[description] = int(number)
        # print(self.description, bag_counts)
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
                # for v in inner.keys():
                #     inner[k] = bags[b].contains[k] * inner[k]
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


    def containCount(self, bags):
        """
        Contains:
        name = val
        name = val
        """
        print(self.description, self.contains)
        for b in self.contains.keys():
            print('  ', )
            bags[b].containCount(bags)
            counter = (self.contains[b] * bags[b].nested_bags) + 1
            self.nested_bags += counter