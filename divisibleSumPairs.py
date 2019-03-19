# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if ((ar[i] + ar[j]) % k == 0):
                count += 1
    return count

print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))