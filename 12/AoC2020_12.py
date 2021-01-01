#!/usr/bin/env python
# coding: utf-8
def rotate(orientation, turn, value):
    if turn == 'L':
        #print('Turning left by ', value)
        orientation = (orientation + value) % 360
    else:
        #print('Turning right by ', value)
        orientation = (orientation - value) % 360
    #print('New orientation is ', orientation)
    return orientation

def move(position, side, value):
    if side == 'E':
        #print('Moving east by ', value)
        position[0] += value
    elif side == 'W':
        #print('Moving west by ', value)
        position[0] -= value
    elif side == 'N':
        #print('Moving north by ', value)
        position[1] += value
    elif side == 'S':
        #print('Moving south by ', value)
        position[1] -= value
    #print('New position is ', position)
    return position

input = open('AoC2020_12_input.txt').read().splitlines()
instructions = [(line[0], int(line[1:])) for line in input]

# Part I
position = [0, 0]
orientation = 0
sides = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}

for i in instructions:
    #print(i)
    if i[0] in ('E', 'W', 'N', 'S'):
        position = move(position, i[0], i[1])
    elif i[0] in ('L', 'R'):
        orientation = rotate(orientation, i[0], i[1])
    elif i[0] == 'F':
        position = move(position, sides[orientation], i[1])

print('Part I = ', abs(position[0]) + abs(position[1]))


# Part II
position = [0, 0]
orientation = 0
sides = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
waypoint_position = [10, 1]
waypoint_orientation = [0, 90]

for i in instructions:
    if i[0] in ('E', 'N', 'W', 'S'):
        waypoint_position = move(waypoint_position, i[0], i[1])
    elif i[0] == 'R':
        if i[1] == 90:
            waypoint_position = [waypoint_position[1], -waypoint_position[0]]
        elif i[1] == 180:
            waypoint_position = [-waypoint_position[0], -waypoint_position[1]]
        elif i[1] == 270:
            waypoint_position = [-waypoint_position[1], waypoint_position[0]]
    elif i[0] == 'L':
        if i[1] == 90:
            waypoint_position = [-waypoint_position[1], waypoint_position[0]]
        elif i[1] == 180:
            waypoint_position = [-waypoint_position[0], -waypoint_position[1]]
        elif i[1] == 270:
            waypoint_position = [waypoint_position[1], -waypoint_position[0]]
    elif i[0] == 'F':
        position = move(position, sides[waypoint_orientation[0]], i[1] * waypoint_position[0])
        position = move(position, sides[waypoint_orientation[1]], i[1] * waypoint_position[1])

print('Part II = ', abs(position[0]) + abs(position[1]))
