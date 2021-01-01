#!/usr/bin/env python
# coding: utf-8
from itertools import combinations

input = open('AoC2020_9_input.txt').read().splitlines()
numbers = [int(line) for line in input]
preamble = 25

def is_valid(position):
    for sm in combinations(numbers[position-preamble:position], 2):
        if sum(sm) == numbers[position]:
            return True
    return False

def find_invalid():
    position = preamble
    while is_valid(position):
        position += 1
    return position

invalid_position = find_invalid()

# Part I
invalid_num = numbers[invalid_position]
print('Part I = ', invalid_num)


def find_sum(invalid_num):
    for i in range(0, len(numbers)-1):
        num_sum = numbers[i]
        for j in range(i+1, len(numbers)):
            num_sum += numbers[j]
            if num_sum == invalid_num:
                return i, j
    return -1, -1

start, end = find_sum(invalid_num)
#print(start, end)

# Part II
res = min(numbers[start: end+1]) + max(numbers[start: end+1])
print('Part II = ', res)
