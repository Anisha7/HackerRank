#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            # row 1
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            #print(arr[i][j],arr[i][j+1], arr[i][j+1])
            # row 2
            sum += arr[i+1][j+1]
            # row 3
            sum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            sums.append(sum)
    
    largest = sums[0]
    for sum in sums:
        if (sum > largest):
            largest = sum
    
    return largest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')

    fptr.close()