#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = s[0:8];
    day = s[8:10];
    if (day == 'AM'):
        if time[0:2] == '12':
            return '00' + time[2:8];
        return time;
    else:
        hour = str(12 + int(s[0:2]));
        if (hour == '24'):
            hour = '12';
        new = hour + time[2:8];
        return new;

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
