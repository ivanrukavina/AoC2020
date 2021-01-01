#!/usr/bin/env python
# coding: utf-8
from collections import defaultdict

def update_count(line, tile_id):
    if line in count:
        count[line][0] += 1
        count[line][1].append(tile_id)
    else:
        count[line] = [1, [tile_id]]

# count the number of hashes in line except for the first and the last character
def count_hash_in_line(line):
    count = 0
    for i in line[1:-1]:
        if i == '#':
            count += 1
    return count

input = open('AoC2020_20_input.txt').read().splitlines()
count = {}
tile_id = 0
row = 0
count_hash = 0
for line in input:
    if line and line[-1] == ':':
        row = 0
        left = []
        right = []
        tile_id = int(line.split(' ')[1].strip(':'))
    elif line:
        left.append(line[0])
        right.append(line[-1])
        row += 1
        if row == 1:
            update_count(line, tile_id)
            update_count(line[::-1], tile_id)
        elif row == 10:
            update_count(''.join(right), tile_id)
            update_count(''.join(right)[::-1], tile_id)
            update_count(line, tile_id)
            update_count(line[::-1], tile_id)
            update_count(''.join(left), tile_id)
            update_count(''.join(left)[::-1], tile_id)
        else:
            # count number of hashes only for the rows from 2 to 9
            count_hash += count_hash_in_line(line)

#print(count)

tiles_count = defaultdict(int)
for i in count:
    for j in count[i][1]:
        tiles_count[j] += count[i][0]

#print(tiles_count)

product = 1
for i in tiles_count:
    if tiles_count[i] == 12:
        #print(i)
        product *= i

print('Part I = ', product)

print(count_hash)
monster_hash = 15
# count if there are monster_number monsters
for monster_number in range(1,20):
    print(count_hash - monster_hash * monster_number)
