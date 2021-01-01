#!/usr/bin/env python
# coding: utf-8
input = [0, 3, 1, 6, 7, 5]

def solve(input, num_turns):
    last_spoken = {}
    for i in range(0, len(input)-1):
        last_spoken[input[i]] = i+1

    previous = input[-1]
    for turn in range(len(input)+1, num_turns):
        #print(' ')
        #print('turn = ', turn)
        if previous in last_spoken:
            #print('last number = ', previous, ' was last spoken ', last_spoken[previous])
            #print('appendam ', turn - last_spoken[input[turn-2]] - 1)
            input.append(turn - last_spoken[input[turn-2]] - 1)
            last_spoken[previous] = turn - 1
            previous = input[turn-1]
        else:
            #print('last number = ', previous, ' was never spoken')
            #print('appendam 0')
            input.append(0)
            last_spoken[previous] = turn - 1
            previous = 0
    return input[-1]

print('Part I = ', solve(input, 2021))
print('Part II = ', solve(input, 30000001))
