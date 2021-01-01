#!/usr/bin/env python
# coding: utf-8
input = open('AoC2020_25_input.txt').read().splitlines()
public_door = int(input[0])
public_card = int(input[1])

def find_loop(subject, public_key):
    prod = 1
    loop = 0
    while prod != public_key:
        #print(prod, public_door)
        prod = prod * subject % 20201227
        loop += 1
    return loop

def find_encryption(subject, loop):
    prod = 1
    for _ in range(loop):
        prod = prod * subject % 20201227
    return prod

loop_door = find_loop(7, public_door)
loop_card = find_loop(7, public_card)
print('Loop size door: ', loop_door)
print('Loop size card: ', loop_card)

print('Encryption key: ', find_encryption(public_card, loop_door))
print('Encryption key: ', find_encryption(public_door, loop_card))
