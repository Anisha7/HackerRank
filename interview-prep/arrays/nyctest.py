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

def isSorted(arr):
    return arr == list(range(1, len(arr) + 1))

def minimumBribes(q):
    count = 0
    # if already sorted
    if (isSorted(q)):
        return count

    l = len(q)
    for i in range(l):
        swapCount = abs(q[i] - i - 1)
        print(q)
        print(q[i], swapCount)
        # at the right index
        if swapCount == 0:
            continue
        elif swapCount > 2:
            print('Too chaotic')
            return
        else:
            if swapCount == 1:
                swap(q, i, i+1)
            elif swapCount == 2:
                swap(q, i, i+1)
                swap(q, i+1, i+2)
            count += swapCount
        
        # if sorted
        if (isSorted(q)):
            return count
    return count


if __name__ == '__main__':
    print("FORWARDS")
    q = [2, 1, 5, 3, 4, 6, 7, 8, 10, 9, 12, 11]
    result = minimumBribes(q)
    print('RESULT: ')
    print(result)
    if (result == 5):
        print('-----*PASSED TEST 1*-----')
    else:
        print('!!!!-----*FAILED TEST 1*-----!!!!')

    q = [2, 5, 1, 3, 4]
    result = minimumBribes(q)
    print('RESULT: ')
    print(result)
    if (result == None):
        print('-----*PASSED TEST 2*-----')
    else:
        print('!!!!-----*FAILED TEST 2*-----!!!!')

    q = [1, 2, 5, 3, 7, 8, 6, 4]
    result = minimumBribes(q)
    print('RESULT: ')
    print(result) # 7
    if (result == 7):
        print('-----*PASSED TEST 3*-----')
    else:
        print('!!!!-----*FAILED TEST 3*-----!!!!')
