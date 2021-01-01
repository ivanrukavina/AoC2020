#!/usr/bin/env python
# coding: utf-8
import re

def check_rules(check, solved, rules):
    result = []
    for c in check:
        if c in solved:
            result.append(solved[c])
        else:
            if c in rules:
                res = check_rules(rules[c], solved, rules)
                result.append(res)
                if c not in solved:
                    solved[c] = res
                else:
                    solved[c].append(res)
            elif c.isalpha():
                solved[c] = c
                result.append(c)
            else:
                result.append('|')
    return result

def create_regex(solved):
    if len(solved) == 1:
        if solved[0] == '|':
            return '|'
        elif len(solved[0]) == 1:
            return '(' + solved[0] + ')'
        else:
            return create_regex(solved[0])
    else:
        res = '('
        for i in range(0, len(solved)):
            res = res + create_regex(solved[i])
        res = res + ')'
        return res

def solve(input):
    rules = {}
    for line in input:
        elems = line.split()
        rules[elems[0].strip(':')] = [elems[i].strip("\"") for i in range(1, len(elems))]

    solved = {}
    regex_0 = check_rules(rules['0'], solved, rules)

    test_regex = create_regex(regex_0)
    test_regex = '^' + test_regex + '$'

    input_string = open('AoC2020_19_input_string.txt').read().splitlines()
    sum = 0
    for line in input_string:
        x = re.search(test_regex, line)
        if x:
            sum += 1
    return sum

input = open('AoC2020_19_input_rules1.txt').read().splitlines()  # Part I
print('Part I = ', solve(input))

input = open('AoC2020_19_input_rules2.txt').read().splitlines()  # Part II
print('Part II = ', solve(input))
