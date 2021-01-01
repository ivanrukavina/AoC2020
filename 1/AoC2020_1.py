#!/usr/bin/env python
# coding: utf-8

input = open('AoC2020_1_input.txt').read().splitlines()
numbers = [int(num) for num in input]

# Part I
for i in numbers:
    for j in numbers:
        if i+j == 2020:
            print(i*j)

# Part II
for i in numbers:
    for j in numbers:
        for k in numbers:
            if i+j+k == 2020:
                print(i*j*k)
