import re

class Bag:
    def __init__(self,desc, bags):
        self.description = desc
        self.contains = {}
        self.contained_by = {}
    
    def getOuterBag(self, s):
        outstring, contents = re.split('contain', s)
        return outstring


    def getInnerBags(self, s):
        """extract a dict of inner bags
        no other == empty
        no comma == single element
        comma = multi element
        """
        outstring, contents = re.split('contain', s)
        # first special case
        bag_counts = {}
        if contents != 'no other bags':
            bags = contents.split(',')
            for bag in bags:
                bag = bag.strip()
                number, description = bag.split(' ', 1)
                description = description.replace(' bags','')
                description = description.replace(' bag', '')
                # print(number)
                bag_counts[description] = number
        return bag_counts
