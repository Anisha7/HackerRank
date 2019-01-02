#!/bin/python3
# Print an integer denoting the minimum number of bribes 
# needed to get the queue into its final state. 
# Print Too chaotic if the state is invalid, i.e. 
# it requires a person to have bribed more than  people.
import math
import os
import random
import re
import sys


def swap(q, i, j):
    if (j >= len(q)):
        return q
    temp = q[i]
    q[i] = q[j]
    q[j] = temp
    return q
    
def place(q, start, i):
    
    # find q[i] in start
    index = start.index(q[i])
    # place it at i and count swaps
    count = 0
    dx = 1
    if (i < index):
        dx = -1
    while (q[i] != start[i]):
        # check for index errors
        if (index + dx < 0 or index + dx >= len(q)):
            print('index error, exiting loop, status: (q, q[i], start[i]) ')
            print(q, q[i], start[i])
            break
        # swap places with index and index +/- 1
        start = swap(start, index, index+dx)
        count += 1
        index += dx
    if (count > 2):
        print('Too chaotic')
        count = None
    return (count, start)

# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    # starting position
    start = list(range(1, len(q)+1))
    
    # check each element in list and place it at the right location
    for i in range(len(q)):
        tup = place(q, start, i)
        if (tup[0] == None):
            count = None
            break
        count += tup[0]
        start = tup[1]
    
    if (count != None):
        print(count)
    return count

if __name__ == '__main__':
    q = [2, 1, 5, 3, 4]
    print('RESULT: ')
    print(minBribes(q))
    q = [2, 5, 1, 3, 4]
    print('RESULT: ')
    print(minBribes(q))
