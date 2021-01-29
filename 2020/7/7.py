#!/usr/bin/env python3
import re
from bag import bag


def getOuterBag(s):
    outstring, contents = re.split('contain', s)
    return outstring

def getInnerBags(s):
    """extract a dict of inner bags"""
    
    outstring, contents = re.split('contain', s)
    contents.strip('\.')
    # first special case
    if contents == 'no other bags':
        return {}
    if re.match(','):
        bags = contents.split(',')
    else:
        bags = ['contents']
    for bag in bags:
        number,description
        

with open('input.txt') as f:
    infile = f.read().splitlines()


my_bag = bag.Bag('shiny gold')
# print(my_bag.description)
outbags = {}



for line in infile:
    outstring = getOuterBag(line)
    # print(outstring)    
