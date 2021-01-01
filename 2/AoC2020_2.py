#!/usr/bin/env python
# coding: utf-8
import re

input = open('AoC2020_2_input.txt').read().splitlines()
sum_part1 = 0
sum_part2 = 0

for line in input:
    char = line.split(" ")[1].strip(':')
    low = int(line.split(" ")[0].split('-')[0])
    high = int(line.split(" ")[0].split('-')[1])
    x = line.split(" ")[2].count(char)
    if x >= low and x <= high:
        sum_part1 += 1
    if ((line.split(" ")[2][low-1] == char and line.split(" ")[2][high-1] != char)
        or (line.split(" ")[2][low-1] != char and line.split(" ")[2][high-1] == char)):
            sum_part2 += 1

print(sum_part1)
print(sum_part2)
