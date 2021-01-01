#!/usr/bin/env python
# coding: utf-8
from collections import deque
import copy

# used for both Part I and Part II
def calculate_score(cards):
    res = 0
    for i in reversed(range(len(cards))):
        res = res + (len(cards) - i) * cards[i]
    return res

# Part I - simulation function
def play_game_v1(cards):
    while cards[0] and cards[1]:
        player = [cards[0].popleft(), cards[1].popleft()]
        #print(player)
        if player[0] > player[1]:
            cards[0].append(player[0])
            cards[0].append(player[1])
        else:
            cards[1].append(player[1])
            cards[1].append(player[0])
        #print(cards)

# Part II - simulation function
def play_game_v2(cards):
    #print(' ')
    #print('Play game')
    visited = []
    while cards[0] and cards[1]:
        res_subgame = 0
        #print('Player 1s deck: ', cards[0])
        #print('Player 2s deck: ', cards[1])
        #print('visited = ', visited)
        if list(cards[0]) in visited or list(cards[1]) in visited:
            #print('Player 1 wins the round because of the recursion!')
            return 1
        else:
            visited.append(list(cards[0]))
            visited.append(list(cards[1]))
            #print('visited = ', visited)
        player = [cards[0].popleft(), cards[1].popleft()]
        #print('Player 1 plays: ', player[0])
        #print('Player 2 plays: ', player[1])
        if player[0] <= len(cards[0]) and player[1] <= len(cards[1]):
            #print(' ')
            #print('Calling subgame...', cards)
            cards_subgame = copy.deepcopy(cards)
            while len(cards_subgame[0]) > player[0]:
                cards_subgame[0].pop()
            while len(cards_subgame[1]) > player[1]:
                cards_subgame[1].pop()
            res_subgame = play_game_v2(cards_subgame)
            #print('Ending subgame...', cards, ' with player ', res_subgame, ' winning')
            #print(' ')
        if res_subgame == 1:
            #print('Player 1 wins the round by winning the subgame')
            #print(' ')
            cards[0].append(player[0])
            cards[0].append(player[1])
        elif res_subgame == 2:
            #print('Player 2 wins the round by winning the subgame')
            #print(' ')
            cards[1].append(player[1])
            cards[1].append(player[0])
        elif player[0] > player[1]:
            #print('Player 1 wins the round')
            #print(' ')
            cards[0].append(player[0])
            cards[0].append(player[1])
        else:
            #print('Player 2 wins the round')
            #print(' ')
            cards[1].append(player[1])
            cards[1].append(player[0])
    if cards[0]:
        #print('Player 1 wins the game!')
        #print(' ')
        return 1
    else:
        #print('Player 2 wins the game!')
        #print(' ')
        return 2


# Input
input = open('AoC2020_22_input.txt').read().splitlines()

# Part I
cards = [deque(), deque()]
player_id = 0
for line in input:
    if line:
        if line.isdigit():
            cards[player_id].append(int(line))
    else:
        player_id += 1

play_game_v1(cards)  # Part I - simulation

print('Part I = ', max(calculate_score(cards[0]), calculate_score(cards[1])))

# Part II
cards = [deque(), deque()]
player_id = 0
for line in input:
    if line:
        if line.isdigit():
            cards[player_id].append(int(line))
    else:
        player_id += 1

play_game_v2(cards)  # Part II - simulation

print('Part II = ', max(calculate_score(cards[0]), calculate_score(cards[1])))
