
def suming(S, m, memo=set()):
    L = list(S)
    if (len(L) < 3):
        return 0
    inc1 = 1
    inc2 = len(L)-1
    for i in range(len(L)):
        while (inc1 < len(L) and inc2 > 0):
            sumed = L[i] + L[inc1] + L[inc2]
            memo.add(sumed)
            inc1 += 1
            inc2 -= 1
    return sum(list(memo))

def sumit(S, m, seen = set()):
    L = list(S)
    if len(L) < 3:
        return 0
    
    result = 0
    for i in range(len(L)-m):
        for j in range(i+1, len(L)-m+1):
            n = j+1
            while n < len(L):
                stuff = L[i]+L[j]+L[n]
                if stuff not in seen:
                    print(L[i],L[j],L[n])
                    print(stuff)
                seen.add(stuff)
                n += 1


                n += 1
    print(seen)
    while (len(seen) > 0):
        result += seen.pop()
    # print(list(seen))
    return result



def sumingRecursiveH(L, m, memo, s = 0, depth = 0):
    print('**********')
    print("depth: ", depth)
    print("L: ", L)
    
    # base case
    if len(L) < m:
        print("exited")
        return
    
    temp = sum(L[:m])
    if temp in memo:
        s += temp
        return

    # else:
    # recursive case
    for i in range(len(L)):
        # print(sum(L[:m]) == temp)
        memo.add(temp)
        print('L[:m]: ',L[:m])
        print("\n")
        s += temp
        # print(memo)
        # print('s: ', s)
        sumingRecursiveH(L[i:i+m-1]+L[i+m:], m, memo, s, depth + 1)
        print('after: ',L[i:i+m-1]+L[i+m:])
        
    return

def sumingRecursive(S, m):
    memo = set()
    sumingRecursiveH(list(S), m, memo)
    result = sum(list(memo))
    return result



def sumitImproved(S, m, counts = dict()):
    L = list(S)
    if len(L) < 3:
        return 0
    
    result = 0
    for i in range(len(L)-m+1):
        for j in range(i+1, len(L)-m+2):
            n = j+1
            while n < len(L):
                # finds each combination
                listSum = L[i]+L[j]+L[n]
                # print(L[i],L[j],L[n])
                # print(listSum)
                # counts its occurences in dictionary
                if listSum in counts.keys():
                    counts[listSum] += 1
                else:
                    counts[listSum] = 1
                n += 1
    # print(counts)
    # adds unique counts to result
    for key in counts:
        if counts[key] == 1:
            result += key
            print(key)
    return result

# print(sumitImproved({1, 3, 6, 8, 10, 11}, 3))
# print(sumitImproved({1, 3, 6, 8, 10, 11}, 4))

def sumRec(L, m, counts=dict(), s=0, depth=''):
    if m == 0:
        # found a set of 3
        # keep its count in dictionary
        if s in counts.keys():
            counts[s] += 1
        else:
            counts[s] = 1
            print(depth + 'sum: ' + str(s))
        return
    
    # recursively call to find each set
    for i in range(len(L)-m+1):
        s += L[i]
        print(depth + str(L[i]))
        sumRec(L[i+1:], m-1, counts, s, depth+' ')
        s -= L[i]

def summ(S, m):
    counts = dict()
    sumRec(list(S), m, counts)
    result = 0
    # adds unique counts to result
    for key in counts:
        if counts[key] == 1:
            result += key
            # print(key)
    return result

print('**')
print(summ({1, 3, 6, 8, 10, 11}, 3))
print('**')
print(summ({1, 3, 6, 8, 10, 11}, 4))
print('**')
print(summ({1, 1, 3, 6, 8, 10, 11, 15, 17}, 10))
print('**')
print(summ({1, 1, 3, 6, 8, 10, 11, 15, 17, 32}, 1))
print('**')
# print('other')
# print(sumitImproved({1, 3, 6, 8, 10, 11}, 3))

# 1 + 3 + 6 = 10
        # 8 = 12
        # 10 = 14
        # 11 = 15
# 1 + 6 + 8 = 15
        # 10 = 17
        # 11 = 18
# 1 + 8 + 10 = 19
        # 11 = 20
# 3 + 6 + 8 = 17
        # 10 = 19
        # 11 = 20
# 3 + 8 + 10
        # 11
# 3 + 10 + 11
# 6 + 8 + 10 = 24
        # 11 = 25


