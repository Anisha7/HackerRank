diagonalDifference.py#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    sum1 = 0;
    sum2 = 0;
    c = 0;

    for r in range(len(arr)):
        sum1 += arr[r][c];
        sum2 += arr[r][len(arr[r])-1-c];
        c += 1;
    
    return abs(sum1 - sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
getting matrix diagonal differencel = len(arr;pos = 0neg = 0zero = 0;;;for i in range(l:if arr[i > 0:pos += 1if arr[i < 0:neg += 1if arr[i == 0:zero += result = [pos/l, neg/l, zero/;return result;float(l)float()float()round proun, 6round, 6round, 6print(result[0d;print(result[1;print(result[2;