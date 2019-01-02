# It should return the minimum number of jumps required, as an integer.

def jumpingOnClouds(c):
    n = len(c)
    jumps = 0
    i = 0
    while i < n-1:
        j1 = i + 1
        j2 = i + 2
        # can she jump over 2 clouds
        if (j2 < n and c[j2] == 0):
            jumps += 1
            i += 2
        # else: can she jump over 1 cloud
        elif (j1 < n and c[j1] == 0):
            jumps += 1
            i += 1
    return jumps
        
if __name__ == '__main__':
    j = jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
    print(j)