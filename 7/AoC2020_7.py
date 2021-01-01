#!/usr/bin/env python
# coding: utf-8
from collections import deque

input = open('AoC2020_7_input.txt').read().splitlines()
rules = {}
for line in input:
    bag = line.split(" contain ")[0].rstrip('s')
    contains = [i.strip('.').split(" ", 1) for i in line.split(" contain ")[1].split(', ')]
    if contains[0][0] != 'no':
        rules[bag] = contains
for i in rules:
    for j in range(0, len(rules[i])):
        rules[i][j][1] = rules[i][j][1].rstrip('s')

rules_inverse = {}
for bag in rules:
    for rule in rules[bag]:
        if rule[1] in rules_inverse:
            rules_inverse[rule[1]].add(bag)
        else:
            rules_inverse[rule[1]] = {bag}

# Part I
shiny = 'shiny gold bag'
queue = deque()
queue.append(shiny)
can_contain = set()

while queue:
    bag = queue.pop()
    if bag in rules_inverse:
        for i in rules_inverse[bag]:
            queue.append(i)
            can_contain.add(i)

print('Part I = ', len(can_contain))

# Part II
shiny = 'shiny gold bag'
queue = deque()
queue.append((shiny, 1))
bags_count = 0

while queue:
    bag = queue.pop()
    if bag[0] in rules:
        for i in rules[bag[0]]:
            queue.append((i[1], bag[1]*int(i[0])))
            bags_count += bag[1]*int(i[0])

print('Part II = ', bags_count)
