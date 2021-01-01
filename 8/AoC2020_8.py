#!/usr/bin/env python
# coding: utf-8
input = open('AoC2020_8_input.txt').read().splitlines()
commands = [line.split(' ') for line in input]

def calculate(commands):
    accumulator = 0
    position = 0
    already_visited = []
    while position not in already_visited and position != len(commands):
        already_visited.append(position)
        if commands[position][0] == 'acc':
            accumulator += int(commands[position][1])
            position += 1
        elif commands[position][0] == 'jmp':
            position += int(commands[position][1])
        else:
            position += 1
    return accumulator, position

res, pos = calculate(commands)

print('Part I = ', res)

def calculate_modified(commands):
    for i in commands:
        if i[0] == 'jmp':
            i[0] = 'nop'
            res, pos = calculate(commands)
            i[0] = 'jmp'
            if pos == len(commands):
                return res
        elif i[0] == 'nop':
            i[0] = 'jmp'
            res, pos = calculate(commands)
            i[0] = 'nop'
            if pos == len(commands):
                return res
    return -1

print('Part I = ', calculate_modified(commands))
