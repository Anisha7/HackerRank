import math
import os
import random
import re
import sys
import copy
# 0, 1, 6, 7 , 8, 12 are working

def find(L, item):
    for listItem in L:
        # if (listItem == item):
        #     return True
        if (set(listItem) == set(item) and len(item) == len(listItem)):
            return True
    return False

def getWaysH(n,c,options, depth = 0, curr = []):
    # print('depth: ', depth)
    # print('options: ', options)
    # print('curr: ', curr)
    currSum = sum(curr) # O(N)

    if (currSum == n and find(options, curr)==False):
        options.append(curr)
        # options.append(copy.deepcopy(curr))
        return
    
    else:
        # for all options
        for coin in c: # O(c) c => # of coins
            # print('coin: ', coin)
            if coin > n or currSum > n or coin > n-currSum or currSum + coin > n:
                break
            else:
                curr.append(coin)
                if (currSum + coin <= n): # O(N)
                    # getWaysH(n,c,options,depth+1,copy.deepcopy(curr))
                    getWaysH(n,c,options,depth+1,copy.copy(curr))
                curr.pop() # O(1)
                
    return


# Complete the getWays function below.
def getWays(n, c):
    options = []
    c.sort()
    # remove unnecessary options
    coins = []
    for coin in c:
        if (coin <= n):
            coins.append(coin)
        else:
            break

    getWaysH(n, coins, options)
    print('in result: ',options)
    if options == None:
        return 0
    return len(options)

if __name__ == '__main__':
    print(getWays(4, [1,2,3])) # 4
    print(getWays(10, [2,5,6])) # 5
    # print(getWays(219, [36, 10, 42, 7, 50, 1, 49, 24, 37, 12, 34, 13, 39, 18, 8, 29, 19, 43, 5, 44, 28, 23, 35, 26]))