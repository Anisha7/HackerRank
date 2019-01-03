#!/bin/python3
# Print an integer denoting the minimum number of bribes 
# needed to get the queue into its final state. 
# Print Too chaotic if the state is invalid, i.e. 
# it requires a person to have bribed more than  people.
#!/bin/python3

import math
import os
import random
import re
import sys

# O(1)
def swap(q, i, j):
    if (j >= len(q)):
        return q
    q[i],q[j] = q[j],q[i]
    return q

# O(N) because of index function
def place(q, start, i):
    
    # find q[i] in start array
    index = start.index(q[i])
    # check count
    # optimization: if too chaotic, function will exit
    count = abs(index - i)
    if (count > 2):
        print('Too chaotic')
        count = None
        return (count, start)

    # alter start array
    dx = 1
    if (i < index):
        dx = -1
    while (i != index):
        # swap places with index and index + dx
        start = swap(start, index, index+dx) # O(1)
        index += dx
    
    return (count, start)

# Worst: O(N**2) where N = len(q)
# Best: O(N) where the first element requires 2+ swaps
def minimumBribes(q):
    count = 0
    # starting position
    start = list(range(1, len(q)+1))
    
    # check each element in list and place it at the right location
    for i in range(len(q)):
        tup = place(q, start, i) # O(1)
        # if too chaotic, exit loop and return
        if (tup[0] == None):
            count = None
            break
        count += tup[0]
        start = tup[1]

        # if equal already, break out of loop
        if (q == start):
            break
    
    if (count != None):
        print(count)
    return
    
if __name__ == '__main__':
    q = [2, 1, 5, 3, 4, 6, 7, 8, 10, 9, 12, 11]
    print('RESULT: ')
    print(minimumBribes(q))
    q = [2, 5, 1, 3, 4]
    print('RESULT: ')
    print(minimumBribes(q))
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    print('RESULT: ')
    print(minimumBribes(q)) # 7