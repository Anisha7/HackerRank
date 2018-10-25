#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    ar.sort();
    if len(ar) == 0:
        print(0);
        return 0;

    max = ar[len(ar)-1];
    count = 1;
    for i in range(len(ar) - 1):
        if (ar[len(ar) - 2 - i] == max):
            count += 1;
    
    print(count);
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
