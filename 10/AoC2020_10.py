#!/usr/bin/env python
# coding: utf-8
input = open('AoC2020_10_input.txt').read().splitlines()
numbers = [int(line) for line in input]

numbers.append(0)
numbers.append(max(numbers)+3)
numbers.sort()

differences = [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]

#print(differences)

count1 = differences.count(1)
count3 = differences.count(3)
#print(count1)
#print(count3)
print('Part I = ', count1 * count3)

from itertools import groupby
b = [sum(1 for i in g) for k,g in groupby(differences) if k==1]

#print(b)

res = 1
for i in b:
    if i <= 3:
        res *= pow(2, i-1)
    else:
        res *= pow(2, i-1) - 1

print('Part II = ', res)
