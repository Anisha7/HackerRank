
def frontTurner(n, p):
    result = 0
    p -= 1
    while (p > 0):
        result += 1
        p -= 2

    return result

def backTurner(n, p):
    result = 0
    if (n != p):
        if n%2 != 0:
            n -= 1

    while (n > p):
        result += 1
        n -= 2
    
    return result

# n = num pages in book
# p = page to turn to
# returns the min number of page turns (starting from front or back)
def pageCount(n, p):
    return min(frontTurner(n, p), backTurner(n,p))

print(pageCount(5,4))
print(pageCount(6,2))