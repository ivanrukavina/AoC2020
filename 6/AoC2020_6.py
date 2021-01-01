#!/usr/bin/env python
# coding: utf-8
from collections import defaultdict

input = open('AoC2020_6_input.txt').read().splitlines()
group = defaultdict(list)
group_id = 0
for line in input:
    if line:
        group[group_id].append(set(line))
    else:
        group_id += 1

sum_anyone = 0
sum_everyone = 0
for i in group:
    anyone = group[i][0].union(*group[i])
    everyone = group[i][0].intersection(*group[i])
    sum_anyone += len(anyone)
    sum_everyone += len(everyone)

print('Part I = ', sum_anyone)
print('Part II = ', sum_everyone)
