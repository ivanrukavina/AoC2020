#!/usr/bin/env python
# coding: utf-8
from collections import defaultdict

input = open('AoC2020_21_input.txt').read().splitlines()
# dictionary that contains a list of ingredient sets
# that potentially have an alergen (the alergen is the key)
contain = defaultdict(list)
# a complete list of ingredients (with duplicates)
ingredient_list = []
for line in input:
    alergens = line.split(' (contains ')[1].strip(')').split(', ')
    ingredients = line.split(' (contains ')[0].split(' ')
    for a in alergens:
        contain[a].append(set(ingredients))
    ingredient_list.extend(ingredients)

# found which ingredient (dictionary key) contains which alergen (dictionary value)
found = {}
# set of ingredients with found alergens
found_set = set([])

found_someting = True
while found_someting:
    found_someting = False
    for alergen in contain:
        # compute the intersection of all the ingredients
        # that potentially contain the selected alergen
        res = contain[alergen][0].intersection(*contain[alergen])
        # push out all the ingredients that are already paired with some alergen
        res = res.difference(found_set)
        # if there is only one potential ingredient left,
        # pair that ingredient with the selected alergen
        if len(res) == 1:
            ingredient = res.pop()
            found[ingredient] = alergen
            found_set.add(ingredient)
            found_someting = True

#print(found)
#print(found_set)

counter = 0
for i in ingredient_list:
    if i not in found_set:
        counter += 1

print('Part I = ', counter)

print('Part II = ', ",".join([k for k, v in sorted(found.items(), key=lambda item: item[1])]))
