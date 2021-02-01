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

# my_bag.canContain(my_bag.description, outbags)

outbags[my_bag.description].canContain(my_bag.description, outbags)

# my_bag.containCount(outbags)
outbags[my_bag.description].containCount(outbags)

print(len(outbags.keys()))
print(len(outbags[my_bag.description].contained_by))
print(outbags[my_bag.description].nested_bags)

# for b in outbags:
#     print(b, outbags[b].contains)