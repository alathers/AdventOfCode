#!/usr/bin/env python3
from bag import bag 
             
my_bag = bag.Bag('shiny gold')
with open('input.txt') as f:
    infile = f.read().splitlines()

outbags = {}
can_contain = []
for line in infile:
    line = line.rstrip('.')
    outstring = my_bag.getOuterBag(line)
    inner_bags = my_bag.getInnerBags(line)
    outbags[outstring] = inner_bags
    if my_bag.description in inner_bags.keys():
        can_contain.append()
    # print(inner_bags)

print(len(can_contain))