#!/usr/bin/env python3
from bag import bag 
             
my_bag = bag.Bag('shiny gold')
# with open('input.txt') as f:
with open('sample_input.txt') as f:
    infile = f.read().splitlines()

outbags = {}
for line in infile:
    line = line.rstrip('.')
    outstring = my_bag.getOuterBag(line)
    outbags[outstring] = bag.Bag(outstring)
    outbags[outstring].setInnerBags(line)


for bag in outbags:
    outbags[bag].populateContains(outbags)

my_bag.canContain(my_bag.description, outbags)
print(len(outbags.keys()))
print(len(my_bag.contained_by))
# print(outbags)