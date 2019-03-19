import sys

maxInt = sys.getrecursionlimit()
# def kangarooHelper(x1, v1, x2, v2, c) :
#     c += 1
#     if c >= 50:
#         return "NO"
#     if (x1 == x2):
#         print(x1,x2)
#         return "YES"
#     if (x1 > x2):
#         return kangarooHelper(x1, v1, x2+v2, v2, c)
#     if (x2 > x1):
#         return kangarooHelper(x1+v1, v1, x2, v2, c)
#     return "NO"

def kangarooHelper(x1, v1, x2, v2, c) :
    c += 1
    if c >= 995:
        print("depth")
        return "NO"
    if (x1 == x2):
        print(x1,x2)
        return "YES"
    return kangarooHelper(x1+v1, v1, x2+v2, v2, c)

def kangaroo(x1, v1, x2, v2) :
    if (x1 == x2):
        print("equal")
        return "YES"
    if (x2 > x1 and v2 > v1):
        print("x2")
        return "NO"
    if (x1 > x2 and v1 > v2):
        print("x1")
        return "NO"
    return kangarooHelper(x1, v1, x2, v2, 0)

# print(kangaroo(0, 3, 4, 2)) # YES
# print(kangaroo(21, 6, 47, 3)) # NO
# print(kangaroo(28, 8, 96, 2)) # NO
# print(kangaroo(42, 3, 94, 2)) # YES
# print(kangaroo(2081, 8403, 9107, 8400)) # YES

# IMPROVED
def mathKangaroo(x1, v1, x2, v2):
    div = v2-v1
    val = x1 - x2
    if (div < 0 and val < 0 or div >= 0 and val >= 0):
        if (val%div == 0):
            return "YES"
    return "NO"

print(mathKangaroo(0, 3, 4, 2)) # YES
print(mathKangaroo(21, 6, 47, 3)) # NO
print(mathKangaroo(28, 8, 96, 2)) # NO
print(mathKangaroo(42, 3, 94, 2)) # YES
print(mathKangaroo(2081, 8403, 9107, 8400)) # YES