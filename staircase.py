#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    spaces = n-1;
    tags = 1;
    for i in range(n):
        line = "";
        for i in range(spaces):
            line += " ";
        for i in range(tags):
            line += "#";
        spaces -= 1;
        tags += 1;
        assert(spaces+tags == n);
        print(line);

if __name__ == '__main__':
    n = int(input())

    staircase(n)
