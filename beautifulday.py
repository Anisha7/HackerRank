def reversedDiff(num):
    old = str(num)
    new = ''
    for i in range(len(old)-1, -1, -1):
        new += old[i]

    return abs(num-int(new))

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    days = 0
    for num in range(i, j+1):
        revDiff = reversedDiff(num)
        if revDiff%k == 0:
            days += 1
    return days