#!/usr/bin/env python
# coding: utf-8
from collections import deque

operands = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operators = ['+', '-', '*', '/']

def precedence(op, part):
    if part == 1:       # Part I
        if op == '+':
            return 1
        elif op == '*':
            return 1
    else:               # Part II
        if op == '+':
            return 2
        elif op == '*':
            return 1

# Transform the expression into postfix notation
def postfix(expression, part):
    stack = deque()
    postfix_queue = deque()
    for c in expression:
        if c in operands:
            postfix_queue.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack:
                s = stack.pop()
                if s == '(': break
                postfix_queue.append(s)
        elif c in operators:
            if not stack or stack[-1] == '(':
                stack.append(c)
            else:
                while stack and stack[-1] != '(' and precedence(c, part) <= precedence(stack[-1], part):
                    postfix_queue.append(stack.pop())
                stack.append(c)
    while stack:
        postfix_queue.append(stack.pop())
    return postfix_queue

# Evaluate the postfix notation expression
def evaluate(postfix_queue):
    stack = deque()
    for c in postfix_queue:
        if c in operands:
            stack.append(c)
        elif c in operators:
            a = stack.pop()
            b = stack.pop()
            stack.append(str(eval(b + c + a)))
    return stack.pop()

def solve(input, part):
    sum = 0
    for line in input:
        line.replace(" ", "")
        postfix_queue = postfix(line, part)
        res = int(evaluate(postfix_queue))
        sum += res
    return sum

input = open('AoC2020_18_input.txt').read().splitlines()

print('Part I = ', solve(input, 1))
print('Part II = ', solve(input, 2))
