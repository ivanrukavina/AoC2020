#!/usr/bin/env python
# coding: utf-8
import re
from collections import defaultdict

def get_coordinates(dc):
    row = dc['se'] + dc['sw'] - dc['nw'] - dc['ne']
    column = dc['se'] - dc['sw'] + dc['ne'] - dc['nw'] + 2 * dc['e'] - 2 * dc['w']
    return (row, column)

def expand_dictionary():
    for i in list(flipped):
        for j in neighbours:
            neighbour_tile = (i[0] + j[0], i[1] + j[1])
            if neighbour_tile not in flipped:
                flipped[neighbour_tile] = 0

# Input
directions_list = ['se', 'sw', 'ne', 'nw', 'e', 'w']
input = open('AoC2020_24_input.txt').read().splitlines()
flipped = defaultdict(int)
for line in input:
    directions = {}
    for d in directions_list:
        directions[d] = len(re.findall(d, line))
        line = re.sub(d, "", line)
    flipped[get_coordinates(directions)] += 1

#print(flipped)

# Part I
count_black = 0
for i in flipped:
    if flipped[i] % 2 != 0:
        count_black += 1
print('Part I = ', count_black)

neighbours = [(0, -2), (0, 2), (-1, -1), (-1, 1), (1, -1), (1, 1)]

# Part II
for day in range(100):
    to_flip = set(())
    expand_dictionary()
    for i in flipped:
        count_black = 0
        for j in neighbours:
            neighbour_tile = (i[0] + j[0], i[1] + j[1])
            if neighbour_tile in flipped and flipped[neighbour_tile] % 2 != 0:
                count_black += 1
        if flipped[i] % 2 != 0:
            if count_black == 0 or count_black > 2:
                to_flip.add(i)
        else:
            if count_black == 2:
                to_flip.add(i)

    for i in to_flip:
        flipped[i] += 1

    count_black = 0
    for i in flipped:
        if flipped[i] % 2 != 0:
            count_black += 1

    #print('Day ', day+1, ' : ', count_black)

print('Part II = ', count_black)
