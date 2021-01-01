#!/usr/bin/env python
# coding: utf-8
import re

def get_id(code):
    row = int(code[:7].replace('F', '0').replace('B', '1'), 2)
    column = int(code[7:].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + column

input = open('AoC2020_5_input.txt').read().splitlines()
max_id = 0
list_id = []
for line in input:
    list_id.append(get_id(line))
    max_id = max(max_id, get_id(line))

# Part I
print('Part I = ', max_id)

def find_gap(list_id):
    for i in range(1, len(list_id)):
        if list_id[i] - list_id[i-1] != 1:
            return list_id[i]-1

# Part II
list_id.sort()
print('Part II = ', find_gap(list_id))
