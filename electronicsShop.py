#
# Complete the getMoneySpent function below.
#

# works but needs optimization
def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()
    maxSum = -1
    # all logical combinations
    for kp in keyboards:
        if (kp >= b):
            continue
        for dp in drives:
            tempSum = kp + dp
            # all sums after will be more
            if (tempSum > b):
                break
            # valid sum, and max
            if (tempSum > maxSum and tempSum <= b):
                if (maxSum == -1):
                    maxSum = 0
                maxSum = tempSum
    return maxSum
