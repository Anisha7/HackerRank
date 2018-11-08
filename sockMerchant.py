#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    #checked = False
    i = 0
    while (i < len(ar)):
        word = ar.pop(i)
        print(ar)
        found = False
        for j in range(len(ar)):
            if (word == ar[j]):
                pairs += 1
                ar.pop(j)
                found = True
                break
        if found == False: 
            i += 1
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
