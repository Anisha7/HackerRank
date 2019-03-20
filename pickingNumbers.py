import collections

# a is sorted and not empty
def removDups(a):
    result = [1]
    prev = a[0]
    i = 1
    while i < len(a):
        if (a[i] == prev):
            result[-1] += 1
            a.pop(i)
        else:
            prev = a[i]
            result.append(1)
            i += 1
        
        
    return result

def fast2(a):
    if len(a) == 0:
        return 0
    a.sort()

    counts = removDups(a)

    maxSum = -1
    for i in range(len(a)-1):
        # print("i:%s"%i)
        e1 = i
        e2 = i+1
        # print(e2, e1)
        if (a[e2]-a[e1]== 1):
            calcSum = counts[e2] + counts[e1]
            if maxSum == -1:
                maxSum = calcSum
            elif calcSum > maxSum:
                maxSum = calcSum

    return maxSum

# nope, not faster
def fast(a):
    if len(a) == 0:
        return 0
    d = collections.Counter(a)
    keys = list(d.keys())
    keys.sort()
    # print(keys)

    maxSum = -1

    for i in range(len(keys)-1):
        # print("i:%s"%i)
        e1 = keys[i]
        e2 = keys[i+1]
        # print(e2, e1)
        if (e2-e1== 1):
            calcSum = d[e2] + d[e1]
            if maxSum == -1:
                maxSum = calcSum
            elif calcSum > maxSum:
                maxSum = calcSum

    return maxSum


def pickingNumbers(a):
    # Write your code here
    a.sort()
    print(a)
    curr = [a[0]]
    maxResult = []
    for i in range(1, len(a)):
        print(maxResult)
        print("curr: ", curr)
        if (a[i]-a[i-1] == 1 and a[i]-a[i-1] == 0):
            found = True
            for elem in curr:
                if (a[i]-elem != 1 and a[i]-elem != 0):
                    print(a[i], elem)
                    found = False

            if (found):
                curr.append(a[i])
            else:
                if (len(maxResult) < len(curr)):
                    print("here")
                    print(len(maxResult))
                    print(len(curr))
                    maxResult = curr
                curr = [a[i]]
    return len(maxResult)


def pickNum(a):
    # empty
    if len(a) == 0:
        return 0
    a.sort()

    curr = [a[0]]
    maxResult = []

    for num in a[1:]:
        print(num, curr, maxResult)
        if (num == curr[-1]):
            curr.append(num)
            # print("Equal, Added")
        elif (abs(num - curr[-1]) == 1):
            found = True
            for elem in curr:
                if (abs(num - elem) != 1 and num != elem):
                    found = False
            if (found):
                curr.append(num)
            # if it does not fit in curr, allocate new curr
            else:
                # print("NEW CURR")
                if len(maxResult) < len(curr):
                    # print("HERE")
                    maxResult = curr
                    # maxResult.extend(curr)
                curr = [num]
        else:
                # print("NEW CURR")
                if len(maxResult) < len(curr):
                    # print("HERE")
                    maxResult = curr
                    # maxResult.extend(curr)
                curr = [num]
    return len(maxResult)

# l = [1, 2, 2, 3, 1, 2] # 5
# print(pickNum(l))
# l = [4, 6, 5, 3, 3, 1]
# print(pickNum(l))

l = [1, 2, 2, 3, 1, 2] # 5
print(fast2(l))
l = [4, 6, 5, 3, 3, 1]
print(fast2(l))