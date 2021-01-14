#!/usr/bin/env python3

from quad_vector import QuadVector

from constellation import Constellation,Constellations


max_mhd = 3

# a set of constellations is really just a
constellation_set = Constellations(max_mhd)


#aim for single pass
with open('input.txt.txt') as f:
    infile = f.read().splitlines()
    for line in infile:
        # print("%s", line)
        point = QuadVector(line.split(','))
        constellation_set.explore(point)

f.closed


print("Total:", constellation_set.count())

# for c in constellation_set.constellations:
#     for p in c.points:
#         print(p.point)
#     print('-------------------------------')