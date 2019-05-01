import sys

'''Helper function for kangaroo: Determine whether a 
denominator and numerator is valid for modular operation'''
def isValid(den, num):
    # both are negative
    if (den < 0 and num < 0):
        return True
    # both are positive
    if (den > 0 and num > 0):
        return True
    return False

''' Given starting positions (x1, x2) of the two kangaroos
and their velocities (v1, v2) meters per jump respectively
Return "YES" if there is a way for the kangaroos to reach 
the same location at the same time
Return "NO" if that is not possible'''
def kangaroo(x1, v1, x2, v2) :
    # math function: distance/velocity == 0 means two points meet
    den = v2-v1 # denominator
    num = x1 - x2 # numerator
    # if both are 0, kangaroo is not moving
    if den == 0 and num == 0:
        return "YES"
    # make sure it is a valid denominator and numerator 
    # for calculating the remainder
    if (isValid(den, num)):
        if (num%den == 0): # if divisible, they meet
            return "YES"
    return "NO"

# can run using pytest or by running the file
def tests():
    assert kangaroo(0, 3, 4, 2) == "YES"
    assert kangaroo(21, 6, 47, 3) == "NO"
    assert kangaroo(28, 8, 96, 2) == "NO"
    assert kangaroo(42, 3, 94, 2) == "YES"
    assert kangaroo(2081, 8403, 9107, 8400) == "YES"
    assert kangaroo(0,0,0,0) == "YES"

if __name__ == "__main__":
    tests()