#!/usr/bin/env python
# coding: utf-8
import re

def validate_passport(passport):
    try:
        for field in passport:
            if field[0] == 'byr':
                if not (int(field[1]) >= 1920 and int(field[1]) <= 2002):
                    return False
            elif field[0] == 'iyr':
                if not (int(field[1]) >= 2010 and int(field[1]) <= 2020):
                    return False
            elif field[0] == 'eyr':
                if not (int(field[1]) >= 2020 and int(field[1]) <= 2030):
                    return False
            elif field[0] == 'hgt':
                if field[1][-2:] in ('cm', 'in'):
                    if field[1][-2:] == 'cm' and not (int(field[1][:-2]) >= 150 and int(field[1][:-2]) <= 193):
                        return False
                    elif field[1][-2:] == 'in' and not (int(field[1][:-2]) >= 59 and int(field[1][:-2]) <= 76):
                        return False
                else:
                    return False
            elif field[0] == 'hcl':
                if field[1][0] != '#':
                    return False
                elif not re.search('^\w+$', field[1][1:]):
                    return False
            elif field[0] == 'ecl':
                if field[1] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                    return False
            elif field[0] == 'pid':
                if not re.search('^(\d{9})$', field[1]):
                    return False
    except:
        return False
    return True

def validate_part1(passports):
    sum_valid = 0
    for i in passports:
        if len(passports[i]) == 7:
            sum_valid += 1
    return sum_valid

def validate_part2(passports):
    sum_valid = 0
    for i in passports:
        if len(passports[i]) == 7 and validate_passport(passports[i]):
            sum_valid += 1
    return sum_valid

input = open('AoC2020_4_input.txt').read().splitlines()
pass_id = 0
passports = {}
passports[0] = set()
for line in input:
    if line:
        for pair in line.split(' '):
            if pair.split(':')[0] != 'cid':
                passports[pass_id].add((pair.split(':')[0], pair.split(':')[1]))
    else:
        pass_id += 1
        passports[pass_id] = set()

sum_valid = validate_part1(passports)
print('Part I = ', sum_valid)

sum_valid = validate_part2(passports)
print('Part II = ', sum_valid)
