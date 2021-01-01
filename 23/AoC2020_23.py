#!/usr/bin/env python
# coding: utf-8
from timeit import default_timer as timer
import numpy as np

class Node:
    def __init__(self, number):
        self.number = number
        self.next = None

    def __repr__(self):
        return 'Node(' + str(self.number) + ')'

class LinkedList:
    def __init__(self):
        self.head = None

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None and len(nodes) > 0:
            node = Node(nodes.pop(0))
            self.head = node
            for i in nodes:
                node.next = Node(i)
                node = node.next
            node.next = self.head

    def __repr__(self):
        node = self.head
        nodes = []
        if node is not None:
            nodes.append(str(node.number))
            node = node.next
        while node is not None and node != self.head:
            nodes.append(str(node.number))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        if node is not None:
            yield node
            node = node.next
        while node is not None and node != self.head:
            yield node
            node = node.next

def listLength(head):
    if head is None:
        return 0
    node = head.next
    count = 1
    while node is not None and node != head:
        count += 1
        node = node.next
    return count

def solve(num_moves, num_cups, current):
    #start = timer()
    for i in range(num_moves):
        #print(' ')
        #print('Move ', i+1)
        #print('Cups: ', llist)
        pickup1 = current.next
        pickup2 = pickup1.next
        pickup3 = pickup2.next
        #print('Pickup: ', pickup1, pickup2, pickup3)
        #print('Current =', current)

        destnum = current.number - 1
        while destnum in [pickup1.number, pickup2.number, pickup3.number] or destnum == 0:
            destnum = destnum - 1 if destnum > 1 else num_cups

        destination = mapping[destnum]
        #print('Destination =', destination)

        current.next = pickup3.next
        pickup3.next = destination.next
        destination.next = pickup1

        current = current.next

        #print('Cups after move: ', llist)
    #end = timer()
    #print('Execution time: ', end - start)

# Part I
input_list = [3, 2, 6, 5, 1, 9, 4, 7, 8]
llist = LinkedList(input_list)
mapping = [0]*(listLength(llist.head)+1)
for i in llist:
    mapping[i.number] = i
solve(100, listLength(llist.head), llist.head)
res = ''.join([str(i.number) for i in llist])
res = res[res.index('1')+1:] + res[:res.index('1')]
print('Part I = ', res)

# Part II
input_list = [3, 2, 6, 5, 1, 9, 4, 7, 8]
input_list += list(range(10,1000001))  # Part II
llist = LinkedList(input_list)
mapping = [0]*(listLength(llist.head)+1)
for i in llist:
    mapping[i.number] = i
solve(10000000, listLength(llist.head), llist.head)
num1 = mapping[1].next.number
num2 = mapping[1].next.next.number
print('Part I = ', num1*num2)
