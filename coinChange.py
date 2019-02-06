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

def getWaysH(n,c,options, depth = 0, curr = [], memo = dict()):
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

def getWaysH2(n,c,memo = dict()):
    
    if n < 0: return 0
    if n == 0: return 1
    if (n,len(c)) in memo.keys(): return memo[(n,len(c))]
    
    else:
        total = 0
        # for all options
        for i in range(len(c)): # O(c) c => # of coins
            coin = c[i]
            if coin > n:
                continue
            else:
                result = getWaysH2(n-coin, c[i:], memo)
                if result > 0: 
                    total += result
                
        memo[(n, len(c))] = total        
        return total


# Complete the getWays function below.
def getWays(n, c):
    options = []
    c.sort()
    
    getWaysH(n, c, options)
    print('in result: ',options)
    if options == None:
        return 0
    return len(options)


# Complete the getWays function below.
memoizing_dict = dict()

# Complete the getWays function below.
def getWaysCOP(n, c):
    global memoizing_dict
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif (n,len(c)) in memoizing_dict.keys():
        return memoizing_dict[(n,len(c))]
    else:
        cum_sum = 0
        for c_index in range(len(c)):
            c_item = c[c_index]
            if c_item > n:
                continue
            else:
                result = getWaysCOP(n-c_item, c[c_index:])
                if result > 0:
                    cum_sum += result
        memoizing_dict[(n,len(c))] = cum_sum
        return cum_sum

if __name__ == '__main__':
    # print(getWaysCOP(4, [1,2,3])) # 4
    # print(getWaysCOP(10, [2,5,6])) # 5
    print(getWaysCOP(219, [36, 10, 42, 7, 50, 1, 49, 24, 37, 12, 34, 13, 39, 18, 8, 29, 19, 43, 5, 44, 28, 23, 35, 26]))
    print(getWaysH2(219, [36, 10, 42, 7, 50, 1, 49, 24, 37, 12, 34, 13, 39, 18, 8, 29, 19, 43, 5, 44, 28, 23, 35, 26]))