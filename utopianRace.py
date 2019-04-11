# Complete the utopianTree function below.
def utopianTree(n):
    add = False
    height = 1
    while n > 0:
        if add == True:
            height += 1
            add = False
        else:
            height *= 2
            add = True
        n -= 1
    return height

print(utopianTree(0)) # 1
print(utopianTree(1)) # 2
print(utopianTree(4)) # 7
print(utopianTree(3)) # 6

