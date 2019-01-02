# A left rotation operation on an array shifts each of the array's elements  unit to the left.
# It should return the resulting array of integers.
# rotLeft has the following parameter(s):
# An array of integers a.
# An integer d, the number of rotations.

def rotLeft(a, d):
    while (d > 0):
        # shift 1 item left
        temp = a[0]
        a.pop(0)
        a.append(temp)
        # change d
        d -= 1
    return a

if __name__ == '__main__':
    print(rotLeft([1,2,3,4,5], 2))