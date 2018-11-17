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

# checks if two lists are equal
def isEqual(l1, l2):
    if (len(l1) != len(l2)):
        return False

    for i in range(len(l1)):
        if (l1[i] != l2[i]):
            return False
    
    return True

# False if bribes > 2 for any elem in dict
def checkBribeCount(d):
    for k in d.keys():
        if (d[k] > 2):
            return False
    return True

# return total bribes made
def countBribes(d):
    count = 0
    for k in d.keys():
        count += d[k]
    return count

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = dict() #track how many bribes
    # initialize dict
    for i in range(len(q)):
        bribes[i] = 0
    
    start = list(range(1, len(q) + 1))
    
    i = len(q) - 1
    while (isEqual(start,q) == False):
        # prevent index out of range
        if (i < 0):
            i = len(q) - 1
        if (q[i] != start[i]):
            # swap
            temp = start[i]
            start[i] = start[i-1]
            start[i-1] = temp
            # add count
            bribes[i] += 1
        
        # increment
        i -= 1

        # check if invalid
        if (checkBribeCount(bribes) == False):
            print('Too chaotic')
            return

    print(countBribes(bribes))
    return

# return index for where num is in q
def find(q, num):
    for i in range(len(q)):
        if (q[i] == num):
            return i
    return -1

def minimumBribes2(q):
    bribes = dict() #track how many bribes
    # initialize dict
    for i in range(len(q)):
        num = i+1
        index = find(q, num)
        if (index != -1):
            bribes[i] = abs(i-index)
        else:
            bribes[i] = 0
    
    if (checkBribeCount(bribes) == False):
        print('Too chaotic')
        return

    print(countBribes(bribes))
    return

if __name__ == '__main__':
    q = [2, 1, 5, 3, 4]
    minimumBribes(q)
    q = [2, 5, 1, 3, 4]
    minimumBribes(q)
