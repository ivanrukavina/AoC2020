#!/usr/bin/env python
# coding: utf-8

def check_slope(input, right, down):
    row = 0
    sum = 0
    for line in input:
        if row % down == 0:
            if line[int(row/down*right) % 31] == '#':
                sum += 1
        row += 1
    return sum

input = open('AoC2020_3_input.txt').read().splitlines()

# Part I
print('Part I = ', check_slope(input, 3, 1))

# Part II
#print(check_slope(input, 1, 1))
#print(check_slope(input, 3, 1))
#print(check_slope(input, 5, 1))
#print(check_slope(input, 7, 1))
#print(check_slope(input, 1, 2))

print('Part II = ',
      check_slope(input, 1, 1) *
      check_slope(input, 3, 1) *
      check_slope(input, 5, 1) *
      check_slope(input, 7, 1) *
      check_slope(input, 1, 2))
