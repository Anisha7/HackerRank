#!/bin/python3

import math
import os
import random
import re
import sys

def julian(year):
    if year%4 == 0:
        return 244
    return 243

def greg(year):
    if (year%400 == 0) or ((year%4 == 0) and (year%100 !=0)):
        return 244
    return 243

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):

    sumOfDays = 0;
    if (year < 1918):
        sumOfDays = julian(year)
    elif (year == 1918):
        sumOfDays = julian(year) - 13
    else:
        sumOfDays = greg(year)

    day = str(256 - sumOfDays)
    if (len(day) < 2) :
        day = '0' + day
    date = day + '.09.' + str(year)
    print(day)
    return date

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
