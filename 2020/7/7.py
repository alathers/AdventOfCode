#!/usr/bin/env python3
import re


def getOuterBag(s):
    outstring, contents = re.split('contain', s)
    return outstring

def getInnerBags(s):
    outstring, contents = re.split('contain', s)
    contents.strip('\.')
    if contents == 'no other bags':
        return {}
    if re.match(','):
        bags = contents.split(,)
    else:
        bags = ['contents']
    for bag in bags:
        number,description
        

with open('input.txt') as f:
    infile = f.read().splitlines()




my_bag = 'shiny gold'
outbags = {}



for line in infile:
    outstring = getOuterBag(line)
    # print(outstring)    
