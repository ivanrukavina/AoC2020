#!/usr/bin/env python
# coding: utf-8
import itertools
import copy

input = open('AoC2020_11_input.txt').read().splitlines()
layout = [list(line) for line in input]
Nrows = len(layout)
Ncolumns = len(layout[0])
for i in layout:
    i.insert(0, '.')
    i.append('.')
layout.insert(0, ['.'] * (Nrows + 2))
layout.append(['.'] * (Nrows + 2))

adjacent_positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def count_around(layout, row, column, state, part):
    count = 0
    for i in adjacent_positions:
        multiplier = 1
        if part == 2:
            while (layout[row+i[0]*multiplier][column+i[1]*multiplier] == '.'
                    and row+i[0]*multiplier > 0 and row+i[0]*multiplier <= Nrows
                    and column+i[1]*multiplier > 0 and column+i[1]*multiplier <= Ncolumns):
                multiplier += 1
        if layout[row+i[0]*multiplier][column+i[1]*multiplier] == state:
            count += 1
    return count

def print_layout(layout):
    for row in range(0, Nrows+2):
        print(''.join(layout[row][0:Ncolumns+2]))

def solve(part, max_occupied, layout):
    change_state = True
    step = 1
    while change_state:
        #print('step = ', step)
        change_state = False
        layout_new = copy.deepcopy(layout)
        for row in range(1, Nrows+1):
            for column in range(1, Ncolumns+1):
                #rint(row, column)
                if layout[row][column] == 'L' and count_around(layout, row, column, '#', part) == 0:
                    #print('become occupied')
                    layout_new[row][column] = '#'
                    change_state = True
                elif layout[row][column] == '#' and count_around(layout, row, column, '#', part) >= max_occupied:
                    #print('become empty')
                    #print(count_around(layout, row, column, '#'))
                    layout_new[row][column] = 'L'
                    change_state = True
        #print_layout(layout_new)
        #print(' ')
        layout = layout_new
        step += 1

    occupied_seats = 0
    for row in layout_new:
        occupied_seats += row.count('#')

    return occupied_seats

#print('Part I = ', solve(layout, 1, 4))
print('Part II = ', solve(layout, 2, 5))
