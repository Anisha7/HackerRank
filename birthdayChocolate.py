# Complete the birthday function below.
def birthday(s, d, m):
    if len(s) < m:
        return []

    count = 0
    for i in range(len(s)):
        if (i+m > len(s)):
            break
        makesum = 0
        for j in range(i, i+m):
            makesum += s[j]
        
        if (makesum == d):
            count += 1
    
    return count


print(birthday([1, 2, 1, 3, 2], 3, 2)) # 2
print(birthday([1, 1, 1, 1, 1, 1], 3, 2)) # 0